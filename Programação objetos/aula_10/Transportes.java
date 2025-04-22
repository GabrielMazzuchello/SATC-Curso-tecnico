import java.util.Scanner;

class Transporte {
    protected String descrição;
    protected double tamanho;
    protected double peso;

    public Transporte(String descrição, double tamanho, double peso) {
        this.descrição = descrição;
        this.tamanho = tamanho;
        this.peso = peso;
    }

    public void dados() {
        System.out.println("Descrição: " + descrição);
        System.out.println("Tamanho: " + tamanho);
        System.out.println("Peso: " + peso);
    }
}

class Aquatico extends Transporte {
    private double altura;

    public Aquatico(String descrição, double tamanho, double peso, double altura) {
        super(descrição, tamanho, peso);
        this.altura = altura;
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    @Override
    public void dados() {
        super.dados();
        System.out.println("Altura: " + altura);
    }
}

class Terrestre extends Transporte {
    private double numeroRodas;

    public Terrestre(String descrição, double tamanho, double peso, double numeroRodas) {
        super(descrição, tamanho, peso);
        this.numeroRodas = numeroRodas;
    }

    public double getNumeroRodas() {
        return numeroRodas;
    }

    public void setNumeroRodas(double numeroRodas) {
        this.numeroRodas = numeroRodas;
    }

    @Override
    public void dados() {
        super.dados();
        System.out.println("Número de rodas: " + numeroRodas);
    }
}

class Aereo extends Transporte {
    private double numeroPassageiros;

    public Aereo(String descrição, double tamanho, double peso, double numeroPassageiros) {
        super(descrição, tamanho, peso);
        this.numeroPassageiros = numeroPassageiros;
    }

    public double getNumeroPassageiros() {
        return numeroPassageiros;
    }

    public void setNumeroPassageiros(double numeroPassageiros) {
        this.numeroPassageiros = numeroPassageiros;
    }

    @Override
    public void dados() {
        super.dados();
        System.out.println("Número de passageiros: " + numeroPassageiros);
    }
}

public class Transportes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Escolha o tipo de Transporte:");
        System.out.println("1 - Aquático");
        System.out.println("2 - Terrestre");
        System.out.println("3 - Aéreo");

        int escolha = scanner.nextInt();
        scanner.nextLine(); // limpa o ENTER

        System.out.println("Descrição: ");
        String descrição = scanner.nextLine();

        System.out.println("Tamanho: ");
        double tamanho = scanner.nextDouble();
        scanner.nextLine(); // limpa o ENTER

        System.out.println("Peso: ");
        double peso = scanner.nextDouble();
        scanner.nextLine(); // limpa o ENTER

        if (escolha == 1) {
            System.out.println("Altura: ");
            double altura = scanner.nextDouble();
            scanner.nextLine();

            Aquatico aquatico = new Aquatico(descrição, tamanho, peso, altura);
            System.out.println("\n🔵 Dados do Transporte Aquático:");
            aquatico.dados();

        } else if (escolha == 2) {
            System.out.println("Número de rodas: ");
            double numeroRodas = scanner.nextDouble();
            scanner.nextLine();

            Terrestre terrestre = new Terrestre(descrição, tamanho, peso, numeroRodas);
            System.out.println("\n🟢 Dados do Transporte Terrestre:");
            terrestre.dados();

        } else if (escolha == 3) {
            System.out.println("Número de passageiros: ");
            double numeroPassageiros = scanner.nextDouble();
            scanner.nextLine();

            Aereo aereo = new Aereo(descrição, tamanho, peso, numeroPassageiros);
            System.out.println("\n🔴 Dados do Transporte Aéreo:");
            aereo.dados();

        } else {
            System.out.println("❌ Opção inválida!");
        }

        scanner.close();
    }
}
