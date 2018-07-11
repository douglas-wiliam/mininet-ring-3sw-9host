""" 

Custom Ring Network Topology builded on Mininet
Class of Computer Networks
Professor: Leobino Nascimento
Students:	Douglas Wiliam F. de Souza <dougl.wil@gmail.com>
		Jorge Lukas Bandarra Barbosa <lukasbandarra@gmail.com>
Three directly connected switches plus three hosts for each one:
          
                    controller
                        |
                        |
                   ____________
                  /            \
     switch______/              \______switch 
    /  |   \     \              /     /  |   \
 host  |  host    \___switch___/   host  |   host
      host            /  |  \           host
                   host  |  host
                       host

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.node import RemoteController


class JougTopo( Topo ):

    def __init__( self, **opts ):

	# Initialize topology
	Topo.__init__( self, **opts )

	# Add hosts and switches
	host1A = self.addHost( 'h1' )
	host2A = self.addHost( 'h2' )
	host3A = self.addHost( 'h3' )

	host1B = self.addHost( 'h4' )
	host2B = self.addHost( 'h5' )
	host3B = self.addHost( 'h6' )

	host1C = self.addHost( 'h7' )
	host2C = self.addHost( 'h8' )
	host3C = self.addHost( 'h9' )

	switchA = self.addSwitch( 's1' )
	switchB = self.addSwitch( 's2' )
	switchC = self.addSwitch( 's3' )

	# Add links
	self.addLink( host1A, switchA )
	self.addLink( host2A, switchA )
	self.addLink( host3A, switchA )

	self.addLink( host1B, switchB )
	self.addLink( host2B, switchB )
	self.addLink( host3B, switchB )

	self.addLink( host1C, switchC )
	self.addLink( host2C, switchC )
	self.addLink( host3C, switchC )
	
	self.addLink( switchA, switchB )
	self.addLink( switchB, switchC )
	self.addLink( switchC, switchA )

#topos = { 'JougTopo': ( lambda: JougTopo() ) }

def main():
	topo = JougTopo()
	net = Mininet(topo = topo, controller = RemoteController)
	net.start()

	#Setting IPs
	h1 = net.get('h1')
	h2 = net.get('h2')
	h3 = net.get('h3')

	h4 = net.get('h4')
	h5 = net.get('h5')
	h6 = net.get('h6')

	h7 = net.get('h7')
	h8 = net.get('h8')
	h9 = net.get('h9')


	h1.setIP('10.10.1.1/24')
	h2.setIP('10.10.1.2/24')
	h3.setIP('10.10.1.3/24')

	h4.setIP('10.10.2.1/24')
	h5.setIP('10.10.2.2/24')
	h6.setIP('10.10.2.3/24')

	h7.setIP('10.10.3.1/24')
	h8.setIP('10.10.3.2/24')
	h9.setIP('10.10.3.3/24')

	for i in xrange(9):
		h = net.get('h%d' % (i + 1))
		h.cmd("ip route add default dev %s-eth0" % ('h%d' % (i + 1)))
		for j in xrange(9):
			h_dst = net.get('h%d' % (j+1))
			h.setARP(h_dst.IP(), h_dst.MAC())
       
	#print "Testando conectividade da rede"
	#net.pingAll()
	
	CLI(net)
	net.stop()

if __name__ == '__main__':
	main()
