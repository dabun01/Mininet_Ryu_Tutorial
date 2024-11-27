from mininet.net import Mininet
from mininet.topolib import TreeTopo

#Create a tree topology with 2 levels and 2 fanout
tree4 = TreeTopo(depth=2,fanout=2)
net = Mininet(topo=tree4)
net.start()
h1, h4  = net.hosts[0], net.hosts[3]
print(h1.cmd('ping -c1 %s' % h4.IP()))
net.stop()

# Create a tree topology with 2 levels and 3 fanout
tree5 = TreeTopo(depth=2,fanout=3)
net = Mininet(topo=tree5)
net.start()
h1, h5  = net.hosts[0], net.hosts[4]
