import java.util.Scanner;

public class ex_03 {
    
    public static void main(String[] args) {
        int[] numeros = new int[3]; 
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            System.out.println("Informe o " + (i + 1) + "° número: ");
            numeros[i] = scanner.nextInt();
        }

        // Chama o método que exibe os números pares
        mostrarNumerosPares(numeros);

        scanner.close();
    }

    public static void mostrarNumerosPares(int[] numeros) {
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] % 2 == 0) {
                System.out.println("O número " + numeros[i] + " é par");
            }
        }
    }
}
