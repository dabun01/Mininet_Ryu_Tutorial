#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import time
import pdb

def emptyNet():
    "Create an empty network and add nodes to it."

    #Create an empty network
    net = Mininet(controller = RemoteController)

    info('*** Adding controller\n')
    net.addController('c0', controller = RemoteController, ip = "10.0.0.2", port = 6633)

    info('*** Adding hosts\n')
    h1 = net.addHost('h1', ip="20.0.0.1")
    h2 = net.addHost('h2', ip="20.0.0.1")

    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    info('*** Creating links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s3)
    SwitchList = [s1, s2, s3, s4]
    for index in range(0, len(SwitchList)):
            for index2 in range(index+1, len(SwitchList)):
                net.addLink(SwitchList[index], SwitchList[index2])

    info('*** Starting network\n')
    net.start()

    info('*** Running CLI\n')
    CLI(net)

    info('*** Stopping network')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()
