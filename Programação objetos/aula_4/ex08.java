package aula_4;

import java.util.Scanner;

public class ex08 {
    public static void main(String[] args) {
        Formacao();
        System.exit(0);
    }

    public static void Formacao() {
        Scanner entrada = new Scanner(System.in);
        
        int fun = 0;
        int med = 0;
        int tec = 0;
        int gra = 0;

        System.out.println("Cadastro de curso");

        System.out.print("Digite a alunos de alunos que serão cadastrados: ");
        int total = entrada.nextInt();

        entrada.nextLine();

        for (int i = 1; i <= total; i++) {

            //System.out.println("Digite o nome do aluno: ");
            //String nome = entrada.nextLine().toUpperCase();

            System.out.println("Digite a sigla do curso\nFUN - Ensino fundamental\nMED - Ensino médio\nTEC - Curso técnico\nGRA - Graduação\n");
            String formacao = entrada.nextLine().toUpperCase();

            if (formacao.equalsIgnoreCase("FUN")) {
               fun++;
            } else if (formacao.equalsIgnoreCase("MED")) {
                med++;
            } else if (formacao.equalsIgnoreCase("TEC")) {
                tec++;
            } else if (formacao.equalsIgnoreCase("GRA")) {
                gra++;
            } else {
                System.out.println("Essa formação não existe, tente novamente!");
            }
        }
        
        System.out.println("Lista dos alunos e suas formações:");
        System.out.println("INF: " + fun);
        System.out.println("MED: " + med);
        System.out.println("ELE: " + tec);
        System.out.println("DES: " + gra);
        entrada.close();
    }
}
