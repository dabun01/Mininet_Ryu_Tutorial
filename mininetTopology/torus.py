#Create a mesh topology with 4 switches and 2 hosts
#This file contains the answer to the mesh topology question
import pdb
from mininet.topo import Topo

class MyTopo( Topo ):
    def __init__(self):
        "Create custom mesh topology"

        #Initialize the mesh topology
        Topo.__init__(self)

        #Add 12 switches
        H1 = self.addHost('h1',ip="10.0.0.3")
        S2 = self.addSwitch('s2')
        S3 = self.addSwitch('s3')
        S4 = self.addHost('h3',ip="10.0.0.6")
        S5 = self.addSwitch('s5')
        S6 = self.addSwitch('s6')
        S7 = self.addSwitch('s7')
        S8 = self.addSwitch('s8')
        S9 = self.addHost('h4',ip="10.0.0.5")
        S10 = self.addSwitch('s10')
        S11 = self.addSwitch('s11')
        H2 = self.addHost('h2', ip="10.0.0.4")

        #Connect the switches in a torus topology
        #First row
        self.addLink(H1, S2)
        self.addLink(S2, S3)
        self.addLink(S3, S4)
        self.addLink(S4, H1)
        #Second row
        self.addLink(S5, S6)
        self.addLink(S6, S7)
        self.addLink(S7, S8)
        self.addLink(S8, S5)
        #Third row
        self.addLink(S9, S10)
        self.addLink(S10, S11)
        self.addLink(S11, H2)
        self.addLink(H2, S9)
        #Connect row 1 to row 2
        self.addLink(H1, S5)
        self.addLink(S2, S6)
        self.addLink(S3, S7)
        self.addLink(S4, S8)
        #Connect row 1 to row 3
        self.addLink(H1, S9)
        self.addLink(S2, S10)
        self.addLink(S3, S11)
        self.addLink(S4, H2)
        #Connect row 2 to row 3
        self.addLink(S5, S9)
        self.addLink(S6, S10)
        self.addLink(S7, S11)
        self.addLink(S8, H2)

topos = { 'mytopo': ( lambda: MyTopo() ) }

