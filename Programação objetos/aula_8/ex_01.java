import java.util.Scanner;

// Uma indústria deseja controlar seus funcionários. Construir um programa JAVA  que onsidere o problema 
// de registrar os nomes dos funcionários, seus respectivos cargos e salários em Arrays (separadas). Após 
// a leitura, imprimir os funcionários, cargos e salários cadastrados.


public class ex_01 {
    public static void main(String[] args) {
        String[] nome = new String[3];
        String[] cargo = new String[3];
        double[] salario = new double[3];
        
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            System.out.println("Informe o nome do "+ (i + 1) +"° : ");
            nome[i] = scanner.nextLine();

            System.out.println("Informe o cargo do "+ (i + 1) +"° : ");
            cargo[i] = scanner.nextLine();

            System.out.println("Informe o salario do "+ (i + 1) +"° : ");
            salario[i] = scanner.nextDouble();
            scanner.nextLine();

        }

        for (int i = 0; i < 3; i++) {
            System.out.println("O funcionario: "+nome[i]+" do cargo: "+cargo[i]+" com o salario de: "+salario[i]+" reais");
        }

    scanner.close();
    }


}