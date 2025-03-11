package aula_3;
import java.util.Scanner;
public class ex4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int fundamental = 0;
        int medio = 0;
        int tecnico = 0;
        int graduacao = 0;

        // Número de alunos a serem cadastrados
        System.out.println("Quantos alunos você deseja cadastrar?");
        int totalAlunos = entrada.nextInt();
        entrada.nextLine(); // Limpa o buffer após nextInt()

        // Laço para cadastrar os dados dos alunos
        for (int i = 1; i <= totalAlunos; i++) {
            // Solicita o nome e formação do aluno
            System.out.println("\nInforme o nome do aluno " + i + ":");
            // String nome = entrada.nextLine();

            System.out.println("Informe a formação do aluno " + i + " (Fundamental, Médio, Tecnico, Graduação):");
            String formacao = entrada.nextLine().toUpperCase();

            switch (formacao) {
                case "FUNDAMENTAL":
                    fundamental++;
                    break;
                case "MÉDIO":
                    medio++;
                    break;
                case "TECNICO":
                    tecnico++;
                    break;
                case "GRADUAÇÃO":
                    graduacao++;
                    break;
                default:
                    System.out.println("Formação inválida! Digite uma formação válida: Fundamental, Médio, Técnico ou Graduação.");
                    break;
            }
        }

        // Exibe os resultados
        System.out.println("\nTotal de alunos em cada formação:");
        System.out.println("Ensino Fundamental: " + fundamental);
        System.out.println("Ensino Médio: " + medio);
        System.out.println("Ensino Técnico: " + tecnico);
        System.out.println("Graduação: " + graduacao);

        entrada.close();
    }
}
