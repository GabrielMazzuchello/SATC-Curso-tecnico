package aula_4;

import java.util.Scanner;

public class ex14 {

    // Método para cadastrar e mostrar os dados dos setores
    public static void cadastrarSetor() {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o nome do setor: ");
        String nomeSetor = scanner.nextLine();
        
        System.out.print("Digite o nome do gerente do setor: ");
        String gerente = scanner.nextLine();
        
        System.out.print("Digite o telefone do setor: ");
        String telefone = scanner.nextLine();
        
        System.out.println("\n--- Dados do Setor ---");
        System.out.println("Nome do Setor: " + nomeSetor);
        System.out.println("Gerente: " + gerente);
        System.out.println("Telefone: " + telefone);

        scanner.close();
    }

    // Método para cadastrar e mostrar os dados dos funcionários
    public static void cadastrarFuncionario() {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o nome do funcionário: ");
        String nomeFuncionario = scanner.nextLine();
        
        System.out.print("Digite o cargo do funcionário: ");
        String cargo = scanner.nextLine();
        
        System.out.print("Digite o salário do funcionário: ");
        double salario = scanner.nextDouble();
        
        System.out.println("\n--- Dados do Funcionário ---");
        System.out.println("Nome: " + nomeFuncionario);
        System.out.println("Cargo: " + cargo);
        System.out.println("Salário: R$ " + salario);

        scanner.close();
    }

    // Método principal que executa o programa
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Opções para o usuário escolher qual operação realizar
        System.out.println("Selecione uma opção:");
        System.out.println("1 - Cadastrar Setor");
        System.out.println("2 - Cadastrar Funcionário");
        System.out.print("Escolha: ");
        int escolha = scanner.nextInt();
        
        scanner.nextLine(); // Consumir a quebra de linha deixada pelo nextInt
        
        if (escolha == 1) {
            cadastrarSetor();
        } else if (escolha == 2) {
            cadastrarFuncionario();
        } else {
            System.out.println("Opção inválida!");
        }

        scanner.close();
    }
}
