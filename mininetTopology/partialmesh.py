#Create a partial mesh topology with 1 switches and 4 hosts
import pdb
from mininet.topo import Topo

class MyTopo( Topo ):
    def __init__(self):
        "Create custom mesh topology"

        #Initialize the mesh topology
        Topo.__init__(self)

        #Add hosts and switches
        S1 = self.addSwitch('s1')
        H1 = self.addHost('h1')
        H2 = self.addHost('h2')
        H3 = self.addHost('h3')
        H4 = self.addHost('h4')

        #Add links in a circular fashion
        self.addLink(H1, H2)
        self.addLink(H2, S1)
        self.addLink(S1, H3)
        self.addLink(H3, H4)
        self.addLink(H4, H1)
        # Add cross links
        self.addLink(H2, H3)
        self.addLink(S1, H4)
