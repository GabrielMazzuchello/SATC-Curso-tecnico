package aula_4;
import java.util.Scanner;

public class ex06 {
    public static double calcular(double valor1, double valor2, String operacao) {
        double resultado = 0;

        switch (operacao.toLowerCase()) {
            case "adição":
                resultado = valor1 + valor2;
                break;
            case "subtração":
                resultado = valor1 - valor2;
                break;
            case "multiplicação":
                resultado = valor1 * valor2;
                break;
            case "divisão":
                if (valor2 != 0) {
                    resultado = valor1 / valor2;
                } else {
                    System.out.println("Erro: Divisão por zero não permitida.");
                    return Double.NaN; 
                }
                break;
            default:
                System.out.println("Operação inválida.");
                return Double.NaN; 
        }

        return resultado;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

     
        System.out.println("Digite o valor 1:");
        double valor1 = scanner.nextDouble();

        System.out.println("Digite o valor 2:");
        double valor2 = scanner.nextDouble();

        
        System.out.println("Escolha a operação (adição, subtração, multiplicação, divisão):");
        scanner.nextLine();  
        String operacao = scanner.nextLine();

        
        double resultado = calcular(valor1, valor2, operacao);

        if (!Double.isNaN(resultado)) {
            System.out.println("Resultado de " + operacao + ": " + resultado);
        }

        scanner.close();
    }
}

