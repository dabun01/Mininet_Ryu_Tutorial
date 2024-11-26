#Create a mesh topology with 4 switches and 2 hosts
#This file contains the answer to the mesh topology question
import pdb
from mininet.topo import Topo

class MyTopo( Topo ):
    def __init__(self):
        "Create custom mesh topology"

        #Initialize the mesh topology
        Topo.__init__(self)

        #Add hosts and switches
        S1 = self.addSwitch('s1')
        S2 = self.addSwitch('s2')
        S3 = self.addSwitch('s3')
        S4 = self.addSwitch('s4')
        H1 = self.addHost('h1', ip='10.0.0.1/24')
        H2 = self.addHost('h2', ip='10.0.0.100/24')
        SwitchList = [S1, S2, S3, S4]

        #Add links this for loop will create a mesh topology
        for index in range(0, len(SwitchList)):
            for index2 in range(index+1, len(SwitchList)):
                self.addLink(SwitchList[index], SwitchList[index2])
        self.addLink(H1, S1)
        self.addLink(H2, S3)

topos = { 'mytopo': ( lambda: MyTopo() ) }

