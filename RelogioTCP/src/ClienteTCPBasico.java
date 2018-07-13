import java.io.ObjectInputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.net.Socket;
import java.util.Date;
import java.util.Scanner;

public class ClienteTCPBasico {

    private static Socket cliente;
    private static ObjectInputStream entrada;
    private static Date tempo;
    private static String ipServidor;

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ip do Servidor: ");
        
        // Pega a string que representa o ip do servidor
        ipServidor = entrada.next();

        //Sincroniza o tempo local
        syncTempoLocal(ipServidor);
    }

    private static void syncTempoLocal(String ipServidor) {
        try {
            cliente = new Socket(ipServidor, 12345);
            entrada = new ObjectInputStream(cliente.getInputStream());
            tempo = (Date) entrada.readObject();

           	System.out.println("Data/hora recebidas do servidor: " + tempo.toString());
            System.out.println("Configurando data/hora locais...");

            String[] tokens = tempo.toString().split(" ");
            String mes = tokens[1].toUpperCase();
            String dia = tokens[2];
            String horario = tokens[3];
            String ano = tokens[5];
            String argumento = dia + " " + mes + " " + ano+ " " + horario;
            String [] comando = {"date","-s", argumento};
          	//String [] comando = {"date", "-s", "10 JAN 1996 16:03:04"};
            System.out.println(executaComando(comando));
            entrada.close();
            cliente.close();
            System.out.println("Conexao encerrada.");
        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }

    private static String executaComando(String [] comando) {
        StringBuffer output = new StringBuffer();

        Process p;

        try {

            p = Runtime.getRuntime().exec(comando);
            p.waitFor();
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line = null;

            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

        } catch (IOException | InterruptedException e) {
        	e.printStackTrace();
        }

        return output.toString();
    }
}
