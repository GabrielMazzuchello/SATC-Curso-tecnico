package aula_4;

import java.util.Scanner;

public class ex03
 {
    public static void main(String[] args) {
        Media();
        System.exit(0);
    }

    public static void Media() {
        Scanner entrada = new Scanner(System.in);
        double nota1, nota2, media;

        System.out.print("Cálculo de média\n\n");

        System.out.print("Insira a primeira nota: ");
        nota1 = entrada.nextDouble();

        System.out.print("Insira a segunda nota: ");
        nota2 = entrada.nextDouble();

        media = (nota1 + nota2) / 2;

        if (media >= 7 && media < 10) {
            System.out.print("O aluno foi aprovado! Sua média foi: " + media);
        }
        else if (media < 7) {
            System.out.print("O aluno foi reprovado! Sua média foi: " + media);
        }
        else if (media == 10) {
            System.out.print("O aluno foi aprovado com distinção pois sua média foi 10! B)");
        }
        else {
            System.out.print("Algo deu errado!");
        }

        entrada.close();
    }
}