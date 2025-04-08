import java.util.Scanner;

public class ex_04 {
    
    public static void main(String[] args) {
        int[] numeros = new int[10]; // Array de 10 elementos
        Scanner scanner = new Scanner(System.in);

        // Solicita ao usuário para inserir 10 números
        for (int i = 0; i < 10; i++) {
            System.out.println("Informe o " + (i + 1) + "° número: ");
            numeros[i] = scanner.nextInt();
        }

        // Chama o método que exibe os números ímpares
        mostrarNumerosImpares(numeros);

        scanner.close();
    }

    // Método que recebe um array de inteiros e exibe os números ímpares
    public static void mostrarNumerosImpares(int[] numeros) {
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] % 2 != 0) {  // Verifica se o número é ímpar
                System.out.println("O número " + numeros[i] + " é ímpar");
            }
        }
    }
}
