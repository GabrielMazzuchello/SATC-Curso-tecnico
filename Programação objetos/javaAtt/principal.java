import java.util.*;

public class principal {
    public static void main(String[] args) {
        ArrayList<Funcionario> equipe = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe quantos funcionários quer adicionar: ");
        int quantidade = scanner.nextInt();
        scanner.nextLine();

        for (int i = 1; i <= quantidade; i++) {
            System.out.println("\nFuncionário #" + i);
            Funcionario f = criarFuncionario(scanner); // vai pro metodo q cria 
            if (f != null) {
                equipe.add(f); // adiciona no arrayList o objeto sendou ou gerente ou dev
            }
        }

        System.out.println("\nFuncionários cadastrados:");
        for (Funcionario f : equipe) {
            System.out.println(""); // apenas para separar (espaço no terminal)
            f.exibirInfo(); // busca dentro do objeto (funci ou geren) o metodo exibirinfo
        }

        scanner.close();
    }

    public static Funcionario criarFuncionario(Scanner scanner) {
        System.out.println("1- Gerente \n2- Desenvolvedor");
        int escolha = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Nome: ");
        String nome = scanner.nextLine();

        System.out.print("Salário: ");
        double salario = scanner.nextDouble();
        scanner.nextLine();

        if (escolha == 1) {
            System.out.print("Departamento: ");
            String departamento = scanner.nextLine();
            return new Gerente(nome, salario, departamento);
        } else if (escolha == 2) {
            System.out.print("Linguagem: ");
            String linguagem = scanner.nextLine();
            return new Desenvolvedor(nome, salario, linguagem);
        } else {
            System.out.println("Opção inválida! Funcionário não será adicionado.");
            return null;
        }
    }
}


// import java.util.*;
// public class principal {
//     public static void main(String[] args) {
//         ArrayList<Funcionario> equipe = new ArrayList<Funcionario>();
//         Scanner scanner = new Scanner(System.in);

//         System.out.println("Informe quantos funcinarios quer adicionar: ");
//         int quantidade = scanner.nextInt();
//         scanner.nextLine();

//         for (int i = 1; i <= quantidade; i++) {
//             System.out.println("1- Gerente \n 2- Desenvolvedor");
//             int escolha = scanner.nextInt();
//             scanner.nextLine();

//             System.out.println("Nome: ");
//             String nome = scanner.nextLine();

//             System.out.println("Salario: ");
//             double salario = scanner.nextDouble();
//             scanner.nextLine();

//             if (escolha == 1) {
//                 System.out.println("Departamento: ");
//                 String departamento = scanner.nextLine();

//                 equipe.add(new Gerente(nome, salario, departamento));
//             } else if (escolha == 2) {
//                 System.out.println("Linguagem: ");
//                 String linguagem = scanner.nextLine();
                
//                 equipe.add(new Desenvolvedor(nome, salario, linguagem));
//             }
//         }
//         System.out.println("Funcionarios cadastrados ");
//         for (Funcionario f : equipe) {
//             f.exibirInfo();
//         }

//         scanner.close();
//     }
    
// }