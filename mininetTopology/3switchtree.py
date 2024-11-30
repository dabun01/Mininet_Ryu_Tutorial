import pdb
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        #for loop to add 6 hosts
        for h in range(1, 7):
            host = self.addHost('h%s' % h)
        # Add links
        self.addLink(switch1, switch2)
        self.addLink(switch1, switch3)
        #for loop to add 3 hosts to switch 2 and 3
        for h in range(1, 4):
            self.addLink('h%s' % h, switch2)
            self.addLink('h%s' % (h+3), switch3)


topos = { 'mytopo': ( lambda: MyTopo() ) }