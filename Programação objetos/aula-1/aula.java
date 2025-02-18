import java.util.Scanner;  // Importação específica para Scanner

// A classe principal deve ser chamada "Main" conforme o enunciado
class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);  // Instanciação do Scanner
        double Celcius, Farenheit;

        System.out.print("Conversor de temperaturas");

        System.out.print(" Digite a temperatura em Celcius: ");
        Celcius = entrada.nextDouble();

        Farenheit = (9 * Celcius + 160) / 5;

        System.out.print("\n A medida convertida é " + Farenheit + "°F\n");
        entrada.close();
    }
}
