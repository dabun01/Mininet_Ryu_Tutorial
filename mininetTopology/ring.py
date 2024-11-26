#Create a ring topology with 3 switches and 3 hosts
#This file contains the answer to the mesh topology question
import pdb
from mininet.topo import Topo

class MyTopo( Topo ):
    def __init__(self):
        "Create custom ring topology"

        #Initialize the ring topology
        Topo.__init__(self)

        #Add hosts and switches
        S1 = self.addSwitch('s1')
        S2 = self.addSwitch('s2')
        S3 = self.addSwitch('s3')
        H1 = self.addHost('h1')
        H2 = self.addHost('h2')
        H3 = self.addHost('h3')

        #Add links to set up the ring topology
        self.addLink(H1, S1)
        self.addLink(H2, S2)
        self.addLink(H3, S3)
        self.addLink(H1, S3)
        self.addLink(H2, S1)
        self.addLink(H3, S2)


topos = { 'mytopo': ( lambda: MyTopo() ) }