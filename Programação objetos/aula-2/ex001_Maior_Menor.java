//  Faça um programa que receba dois números e imprima o maior deles.
import java.util.Scanner;

public class ex001_Maior_Menor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o primeiro valor: ");
        int value1 = scanner.nextInt();
        
        System.out.print("Digite o segundo valor: ");
        int value2 = scanner.nextInt();

        if (value1 > value2) {
            String mensagem = String.format("O maior valor é: %d",value1);
            System.out.println(mensagem);

        } else {
            String mensagem = String.format("O maior valor é: %d",value2);
            System.out.println(mensagem);
        }

        scanner.close();
    }
}
