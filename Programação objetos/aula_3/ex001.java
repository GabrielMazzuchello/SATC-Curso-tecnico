package aula_3;
import java.util.Scanner;

public class ex001 {

    // Método principal (ponto de entrada para o programa)
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        for(int i = 1; i <= 4; i++) {
            // Solicita os dados do aluno
            System.out.println("Informe o nome do aluno:");
            String nome = entrada.nextLine();
            
            System.out.println("Informe a disciplina: ");
            String disciplina = entrada.nextLine();

            System.out.println("Informe a 1° nota: ");
            double nota1 = entrada.nextDouble();
            
            System.out.println("Informe a 2° nota: ");
            double nota2 = entrada.nextDouble();
            
            // Consome a linha em branco deixada pelo nextDouble
            entrada.nextLine();

            // Calcula a média
            double media = (nota1 + nota2) / 2;

            // Verifica a situação do aluno
            if (media < 5) {
                System.out.printf("Aluno %s da disciplina %s foi reprovado com média %.2f\n", nome, disciplina, media);
            } else if (media >= 5 && media < 7) {
                System.out.printf("Aluno %s da disciplina %s está em recuperação com média %.2f\n", nome, disciplina, media);
            } else {
                System.out.printf("Aluno %s da disciplina %s foi aprovado com média %.2f\n", nome, disciplina, media);
            }
        }

        // Fecha o scanner após o uso
        entrada.close();
    }
}
