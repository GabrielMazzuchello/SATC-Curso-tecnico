package aula_5
import java.util.Scanner;

public class ex8 {
    public static void main(String[] args) {
        // Cria um array de tamanho 10 para armazenar os nomes
        String[] pessoas = new String[10];
        Scanner scanner = new Scanner(System.in);
        
        // variavel para verificar nome (true ou false)
        boolean nomeencontrado = false;

        // Solicita ao usuário que insira 10 nomes
        System.out.println("Digite os 10 nomes das pessoas:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Nome " + (i + 1) + ": ");
            pessoas[i] = scanner.nextLine();
        }

        // Solicita ao usuário que insira o nome a ser verificado
        System.out.print("Digite o nome para pesquisar se já foi cadastrado: ");
        String nomeVerificar = scanner.nextLine();

       
        // pesquisar se o nome informado ja foi cadastrado no array
        for (int i = 0; i < 10; i++) {
            if (pessoas[i].equalsIgnoreCase(nomeVerificar)) {
            	nomeencontrado = true;
                break;
            }
        }

        // Exibe o resultado da verificação
        if (nomeencontrado == true) {
            System.out.println("O nome " + nomeVerificar + " já foi cadastrado.");
        } else {
            System.out.println("O nome " + nomeVerificar + " não foi cadastrado.");
        }

        // Fecha o scanner
        scanner.close();
    }
}
