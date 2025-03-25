package aula06;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ex13 {
    
        public void main(String[] args) {
        cursos();
        coordenadores();
        alunos();
    }

    public void cursos(){
        Scanner entrada = new Scanner(System.in);

        String nome = JOptionPane.showInputDialog("Nome:  ");
        String periodo = JOptionPane.showInputDialog("Período:  ");

        JOptionPane.showMessageDialog(null, "O curso de "+nome+"\nAcontece durante o período: "+periodo , "Curso", 0);
        entrada.close();
    }

    public void coordenadores(){
        Scanner entrada = new Scanner(System.in);

        String nome = JOptionPane.showInputDialog("Nome:  ");
        double salario = Double.parseDouble(JOptionPane.showInputDialog("Salário:  "));

        JOptionPane.showMessageDialog(null, "O coordenador "+nome+"\nRecebe um total de R$ "+salario+" de salário", "Coordenador", 0);
        entrada.close();
    }

    public void alunos(){
        Scanner entrada = new Scanner(System.in);

        String nome = JOptionPane.showInputDialog("Nome:  ");
        double idade = Double.parseDouble(JOptionPane.showInputDialog("Idade:  "));
        String sexo = JOptionPane.showInputDialog("Sexo:  ");

        JOptionPane.showMessageDialog(null, "O aluno "+nome+"\nTem: "+idade+" anos\nE é do sexo "+sexo, "Aluno", 0);
        entrada.close();
    }
}
