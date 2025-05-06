import java.util.Scanner;

class Veiculo {
    protected String codigo;
    protected String descricao;
    protected String marca;
    protected String modelo;
    protected String cor;
    protected int ano;
    protected String tamanho;
    protected double peso;

    public Veiculo(String codigo, String descricao, String marca, String modelo, String cor, int ano, String tamanho, double peso) {
        this.codigo = codigo;
        this.descricao = descricao;
        this.marca = marca;
        this.modelo = modelo;
        this.cor = cor;
        this.ano = ano;
        this.tamanho = tamanho;
        this.peso = peso;
    }

    public void dados() {
        System.out.println("Dados do veículo:");
        System.out.println("Código: " + codigo);
        System.out.println("Descrição: " + descricao);
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Cor: " + cor);
        System.out.println("Ano: " + ano);
        System.out.println("Tamanho: " + tamanho);
        System.out.println("Peso: " + peso);
    }

    public void checkList(String data, String hora) {
        // System.out.println("\n CheckList realizado em "+ data +" as "+ hora);
    }

    public void ajustes(String defeitos) {
        // System.out.println("Ajustes realizados: " + defeitos);
    }

    public void limpeza(String data, String hora) {
        // System.out.println("Limpeza realizada em " + data + " as "+ hora);
    }

    public void abastecimento(String tipo, double quantidade) {
        // System.out.println("Abastecimento do tipo: " + tipo + " " + quantidade + " Litros");
    }
}

class Bicicleta extends Veiculo {
    private int numeroDeRodas;

    public Bicicleta(String codigo, String descricao, String marca, String modelo, String cor, int ano, String tamanho, double peso, int numeroDeRodas) {
        super(codigo, descricao, marca, modelo, cor, ano, tamanho, peso);
        this.numeroDeRodas = numeroDeRodas;
    }

    @Override
    public void dados() {
        super.dados();
        System.out.println("Número de Rodas: " + numeroDeRodas);
    }

    @Override
    public void abastecimento(String tipo, double quantidade){
        System.out.println("Bicicleta não requer abastecimento.");
    }
}

class Automovel extends Veiculo {
    private String tipoDeCombustivel;

    public Automovel(String codigo, String descricao, String marca, String modelo, String cor, int ano, String tamanho, double peso, String tipoDeCombustivel) {
        super(codigo, descricao, marca, modelo, cor, ano, tamanho, peso);
        this.tipoDeCombustivel = tipoDeCombustivel;
    }

    @Override
    public void dados() {
        super.dados();
        System.out.println("Tipo de Combustível: " + tipoDeCombustivel);
    }
}

class Caminhao extends Veiculo {
    private int capacidadeDeCarga;

    public Caminhao(String codigo, String descricao, String marca, String modelo, String cor, int ano, String tamanho, double peso, int capacidadeDeCarga) {
        super(codigo, descricao, marca, modelo, cor, ano, tamanho, peso);
        this.capacidadeDeCarga = capacidadeDeCarga;
    }

    @Override
    public void dados() {
        super.dados();
        System.out.println("Capacidade de Carga: " + capacidadeDeCarga + " kg");
    }
}

public class Oficina {

    // Função para realizar o checklist
    private static void realizarChecklist(Scanner scanner, Veiculo veiculo, String[] dadosServicos) {
        System.out.println("Data do checklist:");
        dadosServicos[0] = scanner.nextLine();
        System.out.println("Hora do checklist:");
        dadosServicos[1] = scanner.nextLine();
        veiculo.checkList(dadosServicos[0], dadosServicos[1]);
    }

    // Função para realizar ajustes
    private static void realizarAjustes(Scanner scanner, Veiculo veiculo, String[] dadosServicos) {
        System.out.println("Descrição do defeito para ajuste:");
        dadosServicos[0] = scanner.nextLine();
        veiculo.ajustes(dadosServicos[0]);
    }

    // Função para realizar limpeza
    private static void realizarLimpeza(Scanner scanner, Veiculo veiculo, String[] dadosServicos) {
        System.out.println("Data da limpeza:");
        dadosServicos[0] = scanner.nextLine();
        System.out.println("Hora da limpeza:");
        dadosServicos[1] = scanner.nextLine();
        veiculo.limpeza(dadosServicos[0], dadosServicos[1]);
    }

    // Função para realizar abastecimento
    private static void realizarAbastecimento(Scanner scanner, Veiculo veiculo, String[] dadosServicos) {
        System.out.println("Tipo de abastecimento:");
        dadosServicos[0] = scanner.nextLine();
        System.out.println("Quantidade:");
        dadosServicos[1] = scanner.nextLine();
        double quantidade = Double.parseDouble(dadosServicos[1]);
        veiculo.abastecimento(dadosServicos[0], quantidade);
    }

    // Função para exibir o resumo final
    private static void exibirResumo(Veiculo veiculo, boolean[] realizados, String[][] dadosServicos) {
        System.out.println("\n===== RESUMO FINAL DOS SERVIÇOS =====");
        veiculo.dados();
        System.out.println("\nServiços Realizados:");

        if (realizados[0]) {
            System.out.println("- Checklist em " + dadosServicos[0][0] + " às " + dadosServicos[0][1]);
        }

        if (realizados[1]) {
            System.out.println("- Ajustes realizados: " + dadosServicos[1][0]);
        }

        if (realizados[2]) {
            System.out.println("- Limpeza em " + dadosServicos[2][0] + " às " + dadosServicos[2][1]);
        }

        if (realizados[3]) {
            System.out.println("- Abastecimento: " + dadosServicos[3][0] + " | " + dadosServicos[3][1] + " Litros");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Escolha o tipo de veículo:");
        System.out.println("1 - Bicicleta");
        System.out.println("2 - Automóvel");
        System.out.println("3 - Caminhão");
        int escolha = scanner.nextInt();
        scanner.nextLine(); // limpar o buffer

        System.out.println("Código:");
        String codigo = scanner.nextLine();

        System.out.println("Descrição:");
        String descricao = scanner.nextLine();

        System.out.println("Marca:");
        String marca = scanner.nextLine();

        System.out.println("Modelo:");
        String modelo = scanner.nextLine();

        System.out.println("Cor:");
        String cor = scanner.nextLine();

        System.out.println("Ano:");
        int ano = scanner.nextInt();
        scanner.nextLine();

        System.out.println("Tamanho:");
        String tamanho = scanner.nextLine();

        System.out.println("Peso:");
        double peso = scanner.nextDouble();
        scanner.nextLine();

        Veiculo veiculo = null;

        if (escolha == 1) {
            System.out.println("Número de rodas:");
            int numeroDeRodas = scanner.nextInt();
            scanner.nextLine();
            veiculo = new Bicicleta(codigo, descricao, marca, modelo, cor, ano, tamanho, peso, numeroDeRodas);
        } else if (escolha == 2) {
            System.out.println("Tipo de combustível:");
            String tipoDeCombustivel = scanner.nextLine();
            veiculo = new Automovel(codigo, descricao, marca, modelo, cor, ano, tamanho, peso, tipoDeCombustivel);
        } else if (escolha == 3) {
            System.out.println("Capacidade de carga (kg):");
            int capacidadeDeCarga = scanner.nextInt();
            scanner.nextLine();
            veiculo = new Caminhao(codigo, descricao, marca, modelo, cor, ano, tamanho, peso, capacidadeDeCarga);
        } else {
            System.out.println("Opção inválida!");
        }

        // Armazenamento dos dados dos serviços
        String[][] dadosServicos = new String[4][2]; // checklist, ajustes, limpeza, abastecimento
        boolean[] realizados = new boolean[4];       // controle dos serviços

        if (veiculo != null) {
            veiculo.dados();

            boolean continuar = true;
            while (continuar) {
                System.out.println("\n--- Menu de Serviços ---");
                System.out.println("1 - Realizar Checklist");
                System.out.println("2 - Realizar Ajustes");
                System.out.println("3 - Realizar Limpeza");
                System.out.println("4 - Realizar Abastecimento");
                System.out.println("5 - Finalizar e Exibir Resumo");
                System.out.print("Escolha uma opção: ");
                int opcao = scanner.nextInt();
                scanner.nextLine();

                switch (opcao) {
                    case 1:
                        realizarChecklist(scanner, veiculo, dadosServicos[0]);
                        realizados[0] = true;
                        break;
                    case 2:
                        realizarAjustes(scanner, veiculo, dadosServicos[1]);
                        realizados[1] = true;
                        break;
                    case 3:
                        realizarLimpeza(scanner, veiculo, dadosServicos[2]);
                        realizados[2] = true;
                        break;
                    case 4:
                        realizarAbastecimento(scanner, veiculo, dadosServicos[3]);
                        realizados[3] = true;
                        break;
                    case 5:
                        continuar = false;
                        break;
                    default:
                        System.out.println("Opção inválida.");
                }
            }

            exibirResumo(veiculo, realizados, dadosServicos);
        }

        scanner.close();
    }
}
