//  Faça um programa que receba o preço de três produtos e informe qual produto 
//  você deve comprar, sabendo que a decisão é sempre pelo mais barato.

import java.util.Scanner;

public class ex002_Mais_barato {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o valor do primeiro produto: ");
        double produto1 = scanner.nextDouble();

        System.out.print("Digite o valor do segundo produto: ");
        double produto2 = scanner.nextDouble();

        System.out.print("Digite o valor do terceiro produto: ");
        double produto3 = scanner.nextDouble();
        
        if (produto1 < produto2 && produto1 < produto3) {
            String mensagem = String.format("O produto de menor valor é o produto 1: %.2f", produto1);
            System.out.println(mensagem);
        } else if (produto2 < produto1 && produto2 < produto3) {
            String mensagem = String.format("O produto de menor valor é o produto 2: %.2f", produto2);
            System.out.println(mensagem);
        } else if (produto3 < produto1 && produto3 < produto2) {
            String mensagem = String.format("O produto de menor valor é o produto 3: %.2f", produto3);
            System.out.println(mensagem);
        }

        scanner.close();
    }
}
