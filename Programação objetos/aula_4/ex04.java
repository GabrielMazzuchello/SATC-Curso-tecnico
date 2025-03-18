package aula_4;

import java.util.Scanner;

public class ex04 {
    public static void Cadastro() {
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

    public static void main(String[] args) {
        Cadastro();
        System.exit(0);
        }
}
