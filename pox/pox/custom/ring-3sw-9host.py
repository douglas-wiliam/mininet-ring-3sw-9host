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
from pox.lib.util import dpidToSTr


def _handle_PacketIn (event):
	match = of.ofp_match(event.ofp, event.port)#Match do PacketIn
	nw_src = match.get_nw_src()#Ip de quem envia o packet
	nw_dsr = match.get_nw_dst()#IP de quem recebe o packet
	dpid = match.dpid

	msg = of.ofp_flow_mod()#Encapsula o comando para criação de uma tabela de entrada no switch

	# Se o switch 1 requisitou a regra e teve um missing para um pacote na sua própria rede
	if( (dpid == 1)  && ( nw_src == IPAddr("10.10.1.0",24) ) ):
		
	
	# Se o switch 1 requisitou a regra e teve um missing para um pacote na rede do switch 2	
	elif((dpid == 1)  && ( nw_src == IPAddr("10.10.2.0",24) ) ):

        # Se o switch 1 requisitou a regra e teve um missing para um pacote na rede do switch 3
	elif((dpid == 1)  && ( nw_src == IPAddr("10.10.3.0",24) ) ):

	# Se o switch 2 requisitou a regra e teve um missing para um pacote na rede do switch 1	
	elif((dpid == 2)  && ( nw_src == IPAddr("10.10.1.0",24) ) ):

	# Se o switch 2 requisitou a regra e teve um missing para um pacote na sua própria rede 
	elif((dpid == 2)  && ( nw_src == IPAddr("10.10.2.0",24) ) ):

	# Se o switch 2 requisitou a regra e teve um missing para um pacote na rede do switch 3
	elif((dpid == 2)  && ( nw_src == IPAddr("10.10.3.0",24) ) ):

	# Se o switch 3 requisitou a regra e teve um missing para um pacote na rede do switch 1
        elif((dpid == 3)  && ( nw_src == IPAddr("10.10.1.0",24) ) ):

	# Se o switch 3 requisitou a regra e teve um missing para um pacote na rede do switch 2
        elif((dpid == 3)  && ( nw_src == IPAddr("10.10.2.0",24) ) ):

	# Se o switch 3 requisitou a regra e teve um missing para um pacote na sua própria rede
        elif((dpid == 3)  && ( nw_src == IPAddr("10.10.3.0",24) ) ):



	msg.match.set_nw_dst(IPAddr("10.10.1.0"),24)
	msg.match.set_nw_dst(IPAddr("10.10.2.0"),24)
	msg.match.set_nw_dst(IPAddr("10.10.3.0"),24)
	
