package aula_4;

import java.util.Scanner;

public class ex02 {
    public static void Cadastro() {
        System.out.println("Informe seu nome: ");
         Scanner scanner = new Scanner(System.in);
            String nome = scanner.nextLine();

            // le a idade
            System.out.println("Informe a sua idade: ");
            int idade = scanner.nextInt();
            scanner.nextLine(); // limpa o buffe


        if (idade >= 0 && idade <= 13) {
            System.out.println("O atleta "+nome+" é da categoria infantil");
            
            
        } else if (idade >= 14 && idade <= 17) {
            System.out.println("O atleta "+nome+" é da categoria juvenil");
            
            
        } else if (idade >= 18 && idade <= 40) {
            System.out.println("O atleta "+nome+" é da categoria proficional");
       
            
        } else if (idade > 40) {
            System.out.println("O atleta "+nome+" é da categoria veterano");
       
        }
        scanner.close();
    }
    public static void main(String[] args) {
        Cadastro();

    }
    
}
