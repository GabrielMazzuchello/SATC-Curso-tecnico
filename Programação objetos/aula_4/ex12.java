package aula_4;

import java.util.Scanner;

public class ex12 {
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

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in );

        boolean programa = true;
        while (programa) {
            System.out.println("Selecione uma opção");
            System.out.println("1- Cadastrar setor");
            System.out.println("2- Cadastrar funcionarios");
            System.out.println("3- Sair");
            System.out.println("Escolha: ");
            int escolha = scanner.nextInt();

            if (escolha == 1) {
                cadastrarSetor();
            } else if (escolha == 2) {
                cadastrarFuncionario();
            } else if (escolha == 3) {
                programa = false;
            } else {
                System.out.println("escolha errada");
            }
            scanner.close();
        }  
    }   
}
