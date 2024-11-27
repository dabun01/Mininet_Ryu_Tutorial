"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.

We want to create the topology shown in the comment above
To add a switch use the addSwitch() method it takes a string as an argument
To add a host use the addHost() method it takes a string as an argument
I have included and example of how to add hosts and switches to the topology
 variableName = self.addHost('name')
 For the name you want to use the Mininet naming convention 
 of h1, h2, h3, etc for hosts and s1, s2, s3, etc for switches
"""
import pdb
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        

        # Add links
        


topos = { 'mytopo': ( lambda: MyTopo() ) }