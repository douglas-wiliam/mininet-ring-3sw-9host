"""

Custom Ring Network Topology Controller builded on  Mininet
Class of Computer Networks
Professor: Leobino Nascimento
Students:	Douglas Wiliam F. de Souza <dougl.wil@gmail.com>
		Jorge Lukas Bandarra Barbosa <bandarrabarbosa@gmail.com>

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

from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt
from pox.lib.util import dpidToStr
from pox.lib.addresses import IPAddr, IPAddr6, EthAddr

def _handle_PacketIn (Event):
	print "Entrou Handle Packet In"
	match = of.ofp_match.from_packet(Event.ofp,Event.port)#Match do PacketIn 

	nw_src = match.get_nw_src()#Ip de quem envia o packet
	nw_dst = match.get_nw_dst()#IP de quem recebe o packet
#	dpid = match.ofp.dpid
	dpid = Event.connection.dpid #match com forca

	msg = of.ofp_flow_mod()#Encapsula o comando para criacao de uma tabela de entrada no switch

	print "Ip de Origem = " + "-".join(nw_src)
	# Se o switch i requisitou uma regra, o controlador o orienta a enviar o pacote na porta j
	for i in xrange(1,4):
		print "Entrou for i"
		for j in xrange(1,4):
			print "Entrou for j"
			ip = "10.10." + str(i) + "." + str(j)
			print "Testando IP de origem para " + ip
			if( (dpid == i) and ( nw_src == (IPAddr(ip), 24) )):
				print "Entrou if"
				print "IP:" +  ip
				msg.actions.append(of.ofp_action_output(port = j))
				msg.match.set_nw_dst(match.get_nw_dst())

	Event.connection.send(msg)
	#msg.match.set_nw_dst(IPAddr("10.10.1.0"),24)
	#msg.match.set_nw_dst(IPAddr("10.10.2.0"),24)
	#msg.match.set_nw_dst(IPAddr("10.10.3.0"),24)
	
def launch (reactive = False):
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
