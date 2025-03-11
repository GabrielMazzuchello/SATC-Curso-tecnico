package aula_3;
import java.util.Scanner;
public class ex2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

         int inf = 0;
         int mec = 0; 
         int ele = 0; 
         int des = 0;

        for(int i = 1; i <= 4; i++) {
            System.out.println("Informe o nome do aluno:");
            // String nome = entrada.nextLine();
            
            System.out.println("Informe a disciplina (INF, MEC, ELE, DES): ".toUpperCase());
            String disciplina = entrada.nextLine();

          switch (disciplina) {
            case "INF":
              inf = inf++;
              break;

            case "MEC":
              mec = mec++;
              break;

            case "ELE":
              mec = ele++;
              break;
        
            case "DES":
              des = des++;
              break;
          
            default:
              break;
          }
        }
        System.out.println("Quantidade de alunos de cada curso: ");
        System.out.println("Informatica: "+inf);
        System.out.println("Mecatronica: "+mec);
        System.out.println("eletronica: "+ele);
        System.out.println("des: "+des);
      entrada.close();
    }
       
}
