// Uma clinica deseja controlar seus médicos. Construir um programa JAVA que considere o problema de 
// registrar os nomes dos medicos, nomes das suas especialidades em Arrays (separadas). Após a leitura, 
// imprimir os médicos e especialidades cadastradas.

import java.util.Scanner;

public class ex_02 {
    public static void main(String[] args) {
        String[] medico = new String[3];
        String[] especialização = new String[3];
        
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            System.out.println("Informe o nome do "+ (i + 1) +"° : ");
            medico[i] = scanner.nextLine();

            System.out.println("Informe a especialização do "+ (i + 1) +"° medico : ");
            especialização[i] = scanner.nextLine();

        }

        for (int i = 0; i < 3; i++) {
            System.out.println("O medico: "+medico[i]+" tem a especialização de "+especialização[i]);
        }

    scanner.close();
    }
    
}
