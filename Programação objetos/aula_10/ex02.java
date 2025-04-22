// Arquivo único (exemplo), mas classes separadas
import java.util.Scanner;

class Animal {
    protected String nome;
    protected float comprimento;
    protected int numeroDePatas;
    protected String cor;
    protected String ambiente;
    protected float velocidadeMedia;

    public Animal(String nome, float comprimento, int numeroDePatas, String cor, String ambiente, float velocidadeMedia) {
        this.nome = nome;
        this.comprimento = comprimento;
        this.numeroDePatas = numeroDePatas;
        this.cor = cor;
        this.ambiente = ambiente;
        this.velocidadeMedia = velocidadeMedia;
    }

    public void dados() {
        System.out.println("🐾 Dados do Animal:");
        System.out.println("Nome: " + nome);
        System.out.println("Comprimento: " + comprimento + " cm");
        System.out.println("Patas: " + numeroDePatas);
        System.out.println("Cor: " + cor);
        System.out.println("Ambiente: " + ambiente);
        System.out.println("Velocidade média: " + velocidadeMedia + " m/s");
    }
}

// Subclasse fora da classe Animal
class Peixe extends Animal {
    private String caracteristica;

    public Peixe(String nome, float comprimento, String cor, String ambiente, float velocidadeMedia, String caracteristica) {
        super(nome, comprimento, 0, cor, ambiente, velocidadeMedia);
        this.caracteristica = caracteristica;
    }

    @Override
    public void dados() {
        super.dados();
        System.out.println("Característica: " + caracteristica);
    }
}

// Outra subclasse também fora da Animal
class Cachorro extends Animal {
    public Cachorro(String nome, float comprimento, String cor, float velocidadeMedia) {
        super(nome, comprimento, 4, cor, "Terrestre", velocidadeMedia);
    }

    @Override
    public void dados() {
        super.dados();
        System.out.println("Animal doméstico: Sim");
    }
}

// Classe principal com o main
public class ex02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Escolha o tipo de animal:");
        System.out.println("1 - Peixe");
        System.out.println("2 - Cachorro");

        int escolha = scanner.nextInt();
        scanner.nextLine();

        if (escolha == 1) {
            System.out.print("Nome do peixe: ");
            String nome = scanner.nextLine();

            System.out.print("Comprimento (cm): ");
            float comprimento = scanner.nextFloat();
            scanner.nextLine();

            System.out.print("Cor: ");
            String cor = scanner.nextLine();

            System.out.print("Ambiente: ");
            String ambiente = scanner.nextLine();

            System.out.print("Velocidade média (m/s): ");
            float velocidade = scanner.nextFloat();
            scanner.nextLine();

            System.out.print("Característica: ");
            String caracteristica = scanner.nextLine();

            Peixe peixe = new Peixe(nome, comprimento, cor, ambiente, velocidade, caracteristica);
            peixe.dados();

        } else if (escolha == 2) {
            System.out.print("Nome do cachorro: ");
            String nome = scanner.nextLine();

            System.out.print("Comprimento (cm): ");
            float comprimento = scanner.nextFloat();
            scanner.nextLine();

            System.out.print("Cor: ");
            String cor = scanner.nextLine();

            System.out.print("Velocidade média (m/s): ");
            float velocidade = scanner.nextFloat();
            scanner.nextLine();

            Cachorro cachorro = new Cachorro(nome, comprimento, cor, velocidade);
            cachorro.dados();
        } else {
            System.out.println("Opção inválida.");
        }

        scanner.close();
    }
}