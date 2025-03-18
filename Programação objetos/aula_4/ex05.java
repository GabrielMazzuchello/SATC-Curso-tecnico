package aula_4;
import java.util.Scanner;
import javax.swing.JOptionPane;
public class ex05 {
    
    public static void main(String[] args) {
    Cadastro();
    System.exit(0);
    }

    public static void Cadastro() {
        Scanner entrada = new Scanner(System.in);
        String Nome, Sigla;
    
        Nome = JOptionPane.showInputDialog("Digite seu nome: \n");
        Sigla = JOptionPane.showInputDialog("Digite a sigla do seu estado civil: \n").toUpperCase();
    
        if (Sigla.equals("S")){
            JOptionPane.showMessageDialog(null, "O estado civil de "+Nome+" é o de Solteiro");
        }
        else if (Sigla.equals("C")){
            JOptionPane.showMessageDialog(null, "O estado civil de "+Nome+" é o de Casado");
        }
        else if (Sigla.equals("V")){
            JOptionPane.showMessageDialog(null, "O estado civil de "+Nome+" é o de Viúvo");
        }
        else if (Sigla.equals("D")){
            JOptionPane.showMessageDialog(null, "O estado civil de "+Nome+" é o de Divorciado");
        }
        else {
            JOptionPane.showMessageDialog(null, "Algo deu errado, tente novamente");
        }
        entrada.close();
    }
}