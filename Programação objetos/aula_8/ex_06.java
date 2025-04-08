// Construir um programa JAVA que contenha um método que leia 02 arrays com A e B com 5 números inteiros. 
// Após criar um novo array R com a soma dos valores dos arrays A e B.

import java.util.Scanner;

public class ex_06 {
    public static void main(String[] args) {
        int[] numeros1 = new int[2];
        int[] numeros2 = new int[2];
        int[] soma = new int[2];

        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe os 2 numeros da primeira lista: ");
        for (int i = 0; i < 2; i++) {
            System.out.println("Informe o "+(i + 1)+"° numero");
            numeros1[i] = scanner.nextInt();
            scanner.nextLine();
        }
        
        System.out.println("Informe os 2 numeros da segunda lista: ");
        for (int i = 0; i < 2; i++) {
            System.out.println("Informe o "+(i + 1)+"° numero");
            numeros2[i] = scanner.nextInt();
            scanner.nextLine();
        }

        for (int i = 0; i < 2; i++) {
            soma[i] = numeros1[i] + numeros2[i];
        }

        System.out.println("A soma dos dois vetores são:");
        for (int i = 0; i < 2; i++) {
            System.out.println(soma[i]);
        }
    scanner.close();
    }    
}
