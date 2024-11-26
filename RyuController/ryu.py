#This file is used to define the Ryu controller class. And should allow us to use the Ryu controller in our Mininet topology.
#And call it in the command line with "sudo mn --custom pox.py --controller pox"
from mininet.node import Controller
from os import environ

RYUDIR = environ['HOME'] + '/ryu'  # Adjust this path to your Ryu installation directory

class Ryu(Controller):
    def __init__(self, name, cdir=RYUDIR,
                 command='ryu-manager',
                 cargs='ryu.app.simple_switch_13',  # Replace with the Ryu app(s) you want to run
                 **kwargs):
        Controller.__init__(self, name, cdir=cdir,
                             command=command, cargs=cargs, **kwargs)

controllers = {'ryu': Ryu}