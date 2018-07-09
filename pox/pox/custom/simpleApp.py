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
from pox.lib.util import dpidToStr

log = core.getLogger()


#def _handle_ConnectionUp (event): 
# Essa função lida com os eventos de conexão de swithces, assim que os swithces se conectam na rede eles avisam ao controlador


def _handle_PacketIn (event):

	msg = of.ofp_flow_mod() #Essa Função cria um pacote OpenFlow para setar uma regra em um switch.
	if event.port == 1:
		msg.match.in_port = 1 # Aqui criamos uma regra que executará as devidas actions quando tiver um match com porta de entrada = 1.
		msg.actions.append(of.ofp_action_output(port = 2)) # Aqui criamos uma action para encaminhar para porta 2.
		#Desta forma estamos criando uma regra no switch que encaminhará todos os pacotes que chegaram pela porta 1 para porta 2.

	elif event.port == 2:
		msg.match.in_port = 2 
		msg.actions.append(of.ofp_action_output(port = 1)) 
		

	elif event.port == 3:
		msg.match.in_port = 3 
		msg.actions.append(of.ofp_action_output(port = 1))
		
  
	event.connection.send(msg) # Aqui nós enviamos o pacote que seta a regra no switch para o switch que gerou o evento de packetIn.


	#Também podemos criar um evento de packetOut, que simplesmente encaminha um pacote pro switch, 
	#com uma ação pra ele tomar, sem instanciar uma regra no switch.
	#Abaixo temos um exemplo:
  
	# msg = of.ofp_packet_out() #cria o pacote de packetOut.
	# msg.data = event.ofp #coloca os mesmos dados do pacote original nesse pacote (do pacote que gerou o packet_in).
	# msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD)) # Cria a regra pra o switch fazer um FLOOD com esse pacote.


def launch (reactive = False):
	core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
	#core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
