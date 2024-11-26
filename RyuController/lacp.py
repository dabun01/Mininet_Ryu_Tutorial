# Import necessary modules from Ryu framework
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib import lacplib  # Library for Link Aggregation Control Protocol (LACP)
from ryu.lib.dpid import str_to_dpid
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.app import simple_switch_13  # Base simple switch application

# Define a custom LACP-enabled simple switch class that inherits from SimpleSwitch13
class SimpleSwitchLacp13(simple_switch_13.SimpleSwitch13):
    # Specify the OpenFlow version to be used (OpenFlow 1.3)
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    # Add the LACP library as a context
    _CONTEXTS = {'lacplib': lacplib.LacpLib}

    def __init__(self, *args, **kwargs):
        """
        Initialize the SimpleSwitchLacp13 application.
        """
        super(SimpleSwitchLacp13, self).__init__(*args, **kwargs)
        self.mac_to_port = {}  # MAC address to port mapping per switch
        self._lacp = kwargs['lacplib']  # Reference to the LACP library instance

        # Enable LACP on a switch with DPID 1, using ports 1 and 2
        self._lacp.add(
            dpid=str_to_dpid('0000000000000001'), ports=[1, 2])

    def del_flow(self, datapath, match):
        """
        Delete a specific flow from the given switch datapath.
        """
        ofproto = datapath.ofproto  # OpenFlow protocol
        parser = datapath.ofproto_parser  # OpenFlow message parser

        # Construct a FlowMod message to delete the flow
        mod = parser.OFPFlowMod(
            datapath=datapath,
            command=ofproto.OFPFC_DELETE,  # Command to delete flows
            out_port=ofproto.OFPP_ANY,  # Match any output port
            out_group=ofproto.OFPG_ANY,  # Match any group
            match=match  # Match conditions for the flow to delete
        )
        # Send the FlowMod message to the switch
        datapath.send_msg(mod)

    @set_ev_cls(lacplib.EventPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        """
        Handle Packet-In events from the switch.
        """
        msg = ev.msg  # Extract the OpenFlow message
        datapath = msg.datapath  # Get the switch datapath object
        ofproto = datapath.ofproto  # OpenFlow protocol
        parser = datapath.ofproto_parser  # OpenFlow message parser
        in_port = msg.match['in_port']  # Get the port where the packet was received

        # Parse the incoming packet
        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]  # Extract the Ethernet header

        dst = eth.dst  # Destination MAC address
        src = eth.src  # Source MAC address

        dpid = datapath.id  # Switch Datapath ID (DPID)
        self.mac_to_port.setdefault(dpid, {})  # Initialize MAC-to-port mapping for this switch

        # Log the packet details
        self.logger.info("packet in %s %s %s %s", dpid, src, dst, in_port)

        # Learn the source MAC address to avoid flooding in future
        self.mac_to_port[dpid][src] = in_port

        # Determine the output port for the destination MAC
        if dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]
        else:
            out_port = ofproto.OFPP_FLOOD  # Flood the packet if the destination is unknown

        # Define actions (e.g., forward the packet to the determined output port)
        actions = [parser.OFPActionOutput(out_port)]

        # Install a flow entry for known MAC addresses to optimize forwarding
        if out_port != ofproto.OFPP_FLOOD:
            match = parser.OFPMatch(in_port=in_port, eth_dst=dst)  # Match criteria for the flow
            self.add_flow(datapath, 1, match, actions)  # Install the flow with priority 1

        # Handle the packet payload
        data = None
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data

        # Construct a PacketOut message to forward the packet
        out = parser.OFPPacketOut(
            datapath=datapath, buffer_id=msg.buffer_id,
            in_port=in_port, actions=actions, data=data
        )
        # Send the PacketOut message to the switch
        datapath.send_msg(out)

    @set_ev_cls(lacplib.EventSlaveStateChanged, MAIN_DISPATCHER)
    def _slave_state_changed_handler(self, ev):
        """
        Handle changes in LACP slave state (e.g., port state changes).
        """
        datapath = ev.datapath  # Switch datapath object
        dpid = datapath.id  # Datapath ID of the switch
        port_no = ev.port  # Port number affected by the state change
        enabled = ev.enabled  # Whether the port is enabled or disabled

        # Log the state change
        self.logger.info("slave state changed port: %d enabled: %s", port_no, enabled)

        # Clear flows and MAC mappings if the port state changes
        if dpid in self.mac_to_port:
            for mac in self.mac_to_port[dpid]:
                # Delete flows matching this MAC address
                match = datapath.ofproto_parser.OFPMatch(eth_dst=mac)
                self.del_flow(datapath, match)
            # Remove all MAC mappings for this switch
            del self.mac_to_port[dpid]
        # Reinitialize the MAC-to-port mapping for this switch
        self.mac_to_port.setdefault(dpid, {})