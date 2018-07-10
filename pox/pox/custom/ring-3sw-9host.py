"""

Custom Ring Network Topology Controller builded on  Mininet
Class of Computer Networks
Professor: Leobino Nascimento
Students: Douglas Wiliam F. de Souza


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


def _handle_PacketIn (Event):
	match = of.ofp_match.from_packet(Event.ofp,Event.port)#Match do PacketIn 

	nw_src = match.get_nw_src()#Ip de quem envia o packet
	nw_dst = match.get_nw_dst()#IP de quem recebe o packet
#	dpid = match.ofp.dpid
	dpid = Event.connection.dpid #match com forca

	msg = of.ofp_flow_mod()#Encapsula o comando para criacao de uma tabela de entrada no switch


	# Se o switch i requisitou a regra e teve um missing para um pacote na sua propria rede
	for i in xrange(1,4):
		for j in xrange(1,4):
			if( (dpid == i) and ( nw_src == IPAddr("10.10.%d.%d" %(i) %(j),24) ) ):
				msg.actions.append(of.ofp_action_output(port = j))
				msg.match.set_nw_dst(match.get_nw_dst())

	Event.connection.send(msg)
	#msg.match.set_nw_dst(IPAddr("10.10.1.0"),24)
	#msg.match.set_nw_dst(IPAddr("10.10.2.0"),24)
	#msg.match.set_nw_dst(IPAddr("10.10.3.0"),24)
	
def launch (reactive = False):
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
