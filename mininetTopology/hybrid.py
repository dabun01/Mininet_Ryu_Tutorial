#Create a hybrid topology with 1 switches and 9 hosts

import pdb
from mininet.topo import Topo

class MyTopo( Topo ):
    def __init__(self):
        "Create custom ring topology"

        #Initialize the ring topology
        Topo.__init__(self)

        #Add hosts and switches
        S1 = self.addSwitch('s1')
        H1 = self.addHost('h1')
        H2 = self.addHost('h2')
        H3 = self.addHost('h3')
        H4 = self.addHost('h4')
        H5 = self.addHost('h5')
        H6 = self.addHost('h6')
        H7 = self.addHost('h7')
        H8 = self.addHost('h8')
        H9 = self.addHost('h9')

        #Add links to set up the ring topology
        #connect the switch to the hosts
        self.addLink(H1, S1)
        self.addLink(H6, S1)
        #connect the host1 to the hosts
        self.addLink(H1, H2)
        self.addLink(H1, H3)
        self.addLink(H1, H4)
        self.addLink(H1, H5)
        #connect host6 through host9 to each other in a ring
        self.addLink(H6, H7)
        self.addLink(H7, H8)
        self.addLink(H8, H9)
        self.addLink(H9, H6)


topos = { 'mytopo': ( lambda: MyTopo() ) }