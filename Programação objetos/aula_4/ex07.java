package aula_4;
// Exercicio7 - Construir um programa em JAVA que contenha um método, que leia os dados de 
// 50 funcionários. A partir dos dados de entrada: nome e salário,  verificar o total de funcionários:
// Total que recebem até R$ 3.000
// Total que recebe entre R$ 3000 e R$ 5000
// Total que recebem mais que R$ 5000

import java.util.Scanner;

public class ex07 {
    public static void funcionarios() {
        Scanner scanner = new Scanner(System.in);
        int funcionario3000 = 0;
        int funcionario5000 = 0;
        int funcionario = 0;

        for (int i = 0; i < 5; i++) {
            // System.out.println("Digite o nome do funcionário " + (i + 1) + ":");
            // String nome = scanner.nextLine();

            System.out.println("Digite o salário do funcionário " + (i + 1) + ":");
            double salario = scanner.nextDouble();
            scanner.nextLine(); // Limpar o buffer

            if (salario <= 3000) {
                funcionario3000++;
            } else if (salario > 3000 && salario <= 5000) {
                funcionario5000++;
            } else if (salario > 5000) {
                funcionario++;
            }

            
        }
        System.out.println("Total de funcionarios com salarios até 3000 " + funcionario3000);
        System.out.println("Total de funcionarios com salarios até 5000 " + funcionario5000);
        System.out.println("Total de funcionarios com salarios maiores de 5000 " + funcionario);
        scanner.close();
    }


    public static void main(String[] args) {
        funcionarios();
        System.exit(0);
    }
    
}
