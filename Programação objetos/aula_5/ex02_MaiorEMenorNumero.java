package aula_5;
import java.util.Scanner;

public class MaiorEMenorNumero {
    public static void main(String[] args) {
        // Definindo o número máximo de entradas
        int maxNumeros = 10;

        // Criando o array para armazenar os números fornecidos pelo usuário
        int[] numeros = new int[maxNumeros];

        // Criando um scanner para capturar entradas do usuário
        Scanner scanner = new Scanner(System.in);

        // Informando o usuário sobre o limite de números
        System.out.println("Informe até 10 números inteiros positivos. Para encerrar antes, digite -1.");

        // Variáveis para armazenar o maior e menor número
        int maiorNumero = Integer.MIN_VALUE;
        int menorNumero = Integer.MAX_VALUE;
        int contador = 0;

        // Coletando os números do usuário
        while (contador < maxNumeros) {
            System.out.print("Digite o número " + (contador + 1) + ": ");
            int numero = scanner.nextInt();

            // Condição para terminar a entrada antes de 10 números
            if (numero == -1) {
                break;
            }

            // Armazenando o número no array
            numeros[contador] = numero;

            // Atualizando o maior e menor número
            if (numero > maiorNumero) {
                maiorNumero = numero;
            }
            if (numero < menorNumero) {
                menorNumero = numero;
            }

            // Incrementando o contador
            contador++;
        }

        // Exibindo o maior e o menor número
        System.out.println("\nMaior número: " + maiorNumero);
        System.out.println("Menor número: " + menorNumero);

        // Fechando o scanner após o uso
        scanner.close();
    }
}
