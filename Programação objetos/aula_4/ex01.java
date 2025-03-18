package aula_4;
import java.util.Scanner;



public class ex01 {
    public static void Cadastro() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe seu nome: ");
        String nome = scanner.nextLine();

        // le a idade
        System.out.println("Informe a sua idade: ");
        int idade = scanner.nextInt();
        scanner.nextLine(); // limpa o buffer

        // verifica as idades e a coloca em sua categoria
        if (idade >= 18) {
            System.out.println("O "+nome+" é da maior de idade"); // acresenta +1 à a categoria
            
        } else {
            System.out.println("O "+nome+" é da maior de idade"); // acresenta +1 à a categoria
        }
        scanner.close();
    }
    public static void main(String[] args) {
        Cadastro();
    }
}
