#Create a star topology with 1 switches and 6 hosts

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

        #Add links to set up the ring topology
        #Host 1 will have 2 connections to the switch
        self.addLink(H1, S1)
        self.addLink(H1, S1)
        self.addLink(H2, S1)
        self.addLink(H3, S1)
        self.addLink(H4, S1)


topos = { 'mytopo': ( lambda: MyTopo() ) }