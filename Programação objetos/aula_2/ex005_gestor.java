/* Os gestores da sua empresa resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para 
desenvolver o programa que calcula os reajustes. Portanto, faça um programa que recebe o salário de um colaborador e o 
reajuste segundo o seguinte critério, baseado no salário atual:
Salários até R$ 280,00 (incluindo), receberão aumento de 20%
Salários entre R$ 280,00 e R$ 700,00 (incluindo), receberão aumento de 15%
Salários entre R$ 700,00 e R$ 1500,00 (incluindo), receberão aumento de 10%
Salários de R$ 1500,00 em diante, receberão aumento de 5% */
import java.util.Scanner;

public class ex005_gestor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o salario: ");
        int salario = scanner.nextInt();
        
        if (salario <= 280) {
            double novoSalario = (salario * 0.20) + salario;
            String mensagem = String.format("O maior valor é: %d", salario);
            System.out.println(mensagem);

        } else if (salario > 280 %% salario <= ) {
            String mensagem = String.format("O maior valor é: %d",value2);
            System.out.println(mensagem);
        }

        scanner.close();
    }
}
