package aula_3;
import java.util.Scanner;

// Construir um algoritmo para cadastrar os dados dos 50 funcionários, a partir dos dados de entrada: nome, setor e salário. E verificar o total de funcionários de cada setor.
// Sigla        Cargo       
// A            Almoxarifado        
// P            Produção
// C            Contabilidade
// V            Vendas

public class ex3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int A = 0; // Almoxarifado
        int P = 0; // Produção
        int C = 0; // Contabilidade
        int V = 0; // Vendas
        double salarioTotal = 0;

        // Laço para 50 funcionários
        for(int i = 1; i <= 3; i++) {
            System.out.println("Informe o nome do funcionário:");
            // String nome = entrada.nextLine(); // Leitura do nome do funcionário

            System.out.println("Informe o salário do funcionário:");
            double salario = entrada.nextDouble();
            salarioTotal += salario; // Soma o salário total
            
            entrada.nextLine(); // Limpa o buffer da linha anterior

            System.out.println("Informe o Setor (A, P, C, V): ");
            String setor = entrada.nextLine().toUpperCase(); // Leitura do setor

            // Verificando o setor e incrementando o contador correspondente
            switch (setor) {
                case "A":
                    A++; // Almoxarifado
                    break;
                case "P":
                    P++; // Produção
                    break;
                case "C":
                    C++; // Contabilidade
                    break;
                case "V":
                    V++; // Vendas
                    break;
                default:
                    System.out.println("Setor inválido! Digite apenas A, P, C ou V.");
                    break;
            }
        }

        // Exibindo os resultados
        System.out.println("Quantidade de funcionários de cada setor: ");
        System.out.println("Almoxarifado: " + A);
        System.out.println("Produção: " + P);
        System.out.println("Contabilidade: " + C);
        System.out.println("Vendas: " + V);
        System.out.println("O salário total é: " + salarioTotal);

        entrada.close();
    }
}
