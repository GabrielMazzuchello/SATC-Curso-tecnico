// Uma indústria deseja controlar as temperaturas de uma máquina. 
// Considere o problema de registrar as temperaturas diárias de uma máquina, correspondente ao 
// ano (10 dias) de operação da máquina. O valor de cada dia é armazenado em uma variável 
// interna a uma estrutura array conhecida pela variável-apontador temperatura. 

package aula_5;

import java.util.Scanner;

public class ex01_ControleTemperaturas {
    public static void main(String[] args) {
        // Definindo o número de dias
        int dias = 10;

        // Criando o array para armazenar as temperaturas
        double[] temperatura = new double[dias];

        // Criando o scanner para capturar entradas do usuário
        Scanner scanner = new Scanner(System.in);

        // Inserindo as temperaturas para os 10 dias
        for (int i = 0; i < dias; i++) {
            System.out.print("Informe a temperatura do dia " + (i + 1) + ": ");
            temperatura[i] = scanner.nextDouble();
        }

        // Exibindo as temperaturas registradas
        System.out.println("\nTemperaturas registradas ao longo dos 10 dias:");
        for (int i = 0; i < dias; i++) {
            System.out.println("Dia " + (i + 1) + ": " + temperatura[i] + "°C");
        }

        // Fechar o scanner após o uso
        scanner.close();
    }
}
