package aula_4;
import java.util.Scanner;

public class ex10 {

    // Classe interna para representar um funcionário
    static class Funcionario {
        String nome;
        String cargo;
        double salario;

        Funcionario(String nome, String cargo, double salario) {
            this.nome = nome;
            this.cargo = cargo;
            this.salario = salario;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Definindo os totais por cargo
        double totalAnalistas = 0;
        double totalProgramadores = 0;
        double totalTecnicos = 0;
        double totalGeral = 0;

        // Criando um array para armazenar os 100 funcionários
        Funcionario[] funcionarios = new Funcionario[100];

        // Coleta de dados dos funcionários
        for (int i = 0; i < 100; i++) {
            System.out.println("Digite o nome do funcionário " + (i + 1) + ":");
            String nome = scanner.nextLine();

            System.out.println("Digite o cargo do funcionário (Analista de Sistemas, Programador, Técnico):");
            String cargo = scanner.nextLine();

            System.out.println("Digite o salário do funcionário:");
            double salario = scanner.nextDouble();
            scanner.nextLine(); // Para consumir a nova linha após o salário

            // Criando o funcionário e armazenando no array
            funcionarios[i] = new Funcionario(nome, cargo, salario);

            // Atualizando os totais por cargo
            switch (cargo) {
                case "Analista de Sistemas":
                    totalAnalistas += salario;
                    break;
                case "Programador":
                    totalProgramadores += salario;
                    break;
                case "Técnico":
                    totalTecnicos += salario;
                    break;
                default:
                    System.out.println("Cargo não reconhecido para o funcionário " + nome);
                    break;
            }

            // Atualizando o total geral de salários
            totalGeral += salario;
        }

        // Exibindo os totais
        System.out.println("\nTotal de salários por cargo:");
        System.out.println("Analista de Sistemas: " + totalAnalistas);
        System.out.println("Programador: " + totalProgramadores);
        System.out.println("Técnico: " + totalTecnicos);
        System.out.println("\nSoma total dos salários da empresa: " + totalGeral);

        scanner.close();
    }
}
