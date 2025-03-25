package aula_4;
import java.util.Scanner;

import javax.swing.JOptionPane;

public class ex11 {
    
    public void main(String[] args) {
        profs();
        disciplinas();
    }

    public void profs(){
        Scanner entrada = new Scanner(System.in);

        String nome = JOptionPane.showInputDialog("Nome:  ");
        String formacao = JOptionPane.showInputDialog("Formação:  ");

        JOptionPane.showMessageDialog(null, "O professor que se chama "+nome+"\n Tem a formação em: "+formacao , "Professor", 0);
        entrada.close();
    }

    public void disciplinas(){
        Scanner entrada = new Scanner(System.in);

        String nome = JOptionPane.showInputDialog("Nome:  ");
        double quantidade = Double.parseDouble(JOptionPane.showInputDialog("Quantidade de alunos:  "));

        JOptionPane.showMessageDialog(null, "A disciplina "+nome+"\n Tem um total de: "+quantidade+" aulas", "Disciplina", 0);
        entrada.close();
    }
}
