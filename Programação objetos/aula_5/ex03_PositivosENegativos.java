package aula_5;
import java.util.Scanner;

public class ContagemPositivosENegativos {
    public static void main(String[] args) {
        // Definindo o número de entradas
        int quantidadeNumeros = 10;

        // Criando o array para armazenar os números fornecidos pelo usuário
        int[] numeros = new int[quantidadeNumeros];

        // Criando um scanner para capturar entradas do usuário
        Scanner scanner = new Scanner(System.in);

        // Variáveis para contar números positivos e negativos
        int positivos = 0;
        int negativos = 0;

        // Coletando os números do usuário
        for (int i = 0; i < quantidadeNumeros; i++) {
            System.out.print("Digite o número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();

            // Verificando se o número é positivo ou negativo
            if (numeros[i] > 0) {
                positivos++;
            } else if (numeros[i] < 0) {
                negativos++;
            }
        }

        // Exibindo o resultado
        System.out.println("\nQuantidade de números positivos: " + positivos);
        System.out.println("Quantidade de números negativos: " + negativos);

        // Fechar o scanner após o uso
        scanner.close();
    }
}
