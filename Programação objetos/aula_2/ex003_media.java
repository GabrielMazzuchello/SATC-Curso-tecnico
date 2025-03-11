/*  Faça um programa que receba duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. */

import java.util.Scanner;

public class ex003_media {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.print("Digite a primeira Nota: ");
    int nota1 = scanner.nextInt();

    System.out.print("Digite a segunda Nota: ");
    int nota2 = scanner.nextInt();

    double media = (nota1 + nota2) / 2;

    if (media == 10) {
      String mensagem = String.format(
        "A media é: %.2f e o aluno foi aprovado com Distinção",
        media
      );
      System.out.println(mensagem);
    } else if (media >= 7 && media <= 10) {
      String mensagem = String.format(
        "A media é: %.2f e o aluno foi aprovado",
        media
      );
      System.out.println(mensagem);
    } else if (media < 7 && media >= 0) {
      String mensagem = String.format(
        "A media é: %.2f e o aluno foi reprovado",
        media
      );
      System.out.println(mensagem);
    } else {
      System.out.println("Nota invalida");
    }

    scanner.close();
  }
}
