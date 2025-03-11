package aula_3;
import java.util.Scanner;
public class ex5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int menorIdade = 0;
        int maiorIdade = 0;
        int feminino = 0;
        int masculino = 0;

        for (int i = 1;i <= 3; i++) {
            System.err.println("Informe o nome: ");
            // String nome = entrada.nextLine();

            System.err.println("Informe o idade: ");
            int idade = entrada.nextInt();

            entrada.nextLine();

            System.err.println("Informe o sexo F (feminino) M (masculino): ");
            String sexo = entrada.nextLine().toUpperCase();

            if (idade < 18) {
                menorIdade++;
            } else {
                maiorIdade++;
            }

            switch (sexo) {
                case "M":
                    masculino++;
                    break;
                
                case "F":
                    feminino++;
                    break;

                default:
                    System.out.println("F ou M");
                    break;
            }
        }  
        System.out.println("A quantidade de alunos menor de idade é: "+menorIdade);    
        System.out.println("A quantidade de alunos maior de idade é: "+maiorIdade);    
        System.out.println("A quantidade de alunos feminino: "+feminino);    
        System.out.println("A quantidade de alunos masculino: "+masculino);    
        entrada.close();
    }  
}
