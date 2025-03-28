package aula_4;

import java.util.Scanner;

public class ex09 {
    public static void classificação() {
        Scanner scanner = new Scanner(System.in);

        String[] nomes = new String[100];
        int[] idades = new int[100];
        char[] sexos = new char[100];

        int maiorDeIdade = 0;
        int menorDeIdade = 0;
        int masculino = 0;
        int feminino = 0;

        for (int i = 0; i < 100; i++) {
            System.out.println("Digite o nome do aluno " + (i + 1) + ":");
            nomes[i] = scanner.nextLine();

            System.out.println("Digite a idade do aluno " + (i + 1) + ":");
            idades[i] = scanner.nextInt();

            System.out.println("Digite o sexo do aluno " + (i + 1) + " (M/F):");
            sexos[i] = scanner.next().toUpperCase().charAt(0);
            scanner.nextLine(); // Limpar o buffer

            if (idades[i] >= 18) {
                maiorDeIdade++;
            } else {
                menorDeIdade++;
            }

            if (sexos[i] == 'M') {
                masculino++;
            } else if (sexos[i] == 'F') {
                feminino++;
            }
        }

        System.out.println("Total de alunos maiores de idade: " + maiorDeIdade);
        System.out.println("Total de alunos menores de idade: " + menorDeIdade);
        System.out.println("Total de alunos do sexo masculino: " + masculino);
        System.out.println("Total de alunos do sexo feminino: " + feminino);

        scanner.close();
    
        
    }

    public static void main(String[] args) {
        classificação();
        System.exit(0);
    }
}
