import java.util.Scanner;
public class ex_05 {
    public static void main(String[] args) {
        int[] numerosNegativos = new int[3];
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            System.out.println("Informe o " + (i + 1) + "° número: ");
            numerosNegativos[i] = scanner.nextInt();
        }

        mostrarNumerosNegativos(numerosNegativos);

        scanner.close();
    }

    public static void mostrarNumerosNegativos(int[] numerosNegativos) {
        for (int i = 0; i < numerosNegativos.length; i++) {
            if (numerosNegativos[i] < 0) {
                System.out.println("O número " + numerosNegativos[i] + " é negativo");
            }
        }
    }
}