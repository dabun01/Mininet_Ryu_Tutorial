

import pdb
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches (Note: add an IP address for each host)
        

        # Add links (Try to use a for loop)
        


topos = { 'mytopo': ( lambda: MyTopo() ) }