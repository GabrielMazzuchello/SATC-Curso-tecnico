import java.util.Scanner;

class funcionario {
    protected String codigo;
    protected String nome;
    protected String sexo;
    protected int numeroDeHoras;
    protected double valorHora;

    public funcionario(String codigo, String nome, String sexo, int numeroDeHoras, double valorHora) {
        this.codigo = codigo;
        this.nome = nome;
        this.sexo = sexo;
        this.numeroDeHoras = numeroDeHoras;
        this.valorHora = valorHora;

    }

    public void dados() {
        System.out.println("Código: " + codigo);
        System.out.println("Nome: " + nome);
        System.out.println("Sexo: " + sexo);
        System.out.println("Número de Horas: " + numeroDeHoras);
        System.out.println("Valor da Hora: " + valorHora);
    }
}

class Engenheiro extends funcionario {
    private String crea;
    private String especialidade;

    public Engenheiro(String codigo, String nome, String sexo, int numeroDeHoras, double valorHora, String especialidade, String crea) {
        super(codigo, nome, sexo, numeroDeHoras, valorHora);
        this.especialidade = especialidade;
        this.crea = crea;
    }

    @Override
    public void dados() {
        super.dados();
        System.out.println("Especialidade: " + especialidade);
        System.out.println("CREA: " + crea);
    }
}

class Diretor extends funcionario {
    private String areaGestao;

    public Diretor(String codigo, String nome, String sexo, int numeroDeHoras, double valorHora, String areaGestao) {
        super(codigo, nome, sexo, numeroDeHoras, valorHora);
        this.areaGestao = areaGestao;
    }

    @Override
    public void dados() {
        super.dados();
        System.out.println("Área de Gestão: " + areaGestao);
    }
}

class Secretario extends funcionario {
    private String categoria;
    private String setor;

    public Secretario(String codigo, String nome, String sexo, int numeroDeHoras, double valorHora, String categoria, String setor) {
        super(codigo, nome, sexo, numeroDeHoras, valorHora);
        this.categoria = categoria;
        this.setor = setor;
    }
    @Override
    public void dados() {
        super.dados();
        System.out.println("Categoria: " + categoria);
        System.out.println("Setor: " + setor);
    }
}

class Gerente extends funcionario {
    private String setor;

    public Gerente(String codigo, String nome, String sexo, int numeroDeHoras, double valorHora, String setor) {
        super(codigo, nome, sexo, numeroDeHoras, valorHora);
        this.setor = setor;
    }

    @Override
    public void dados() {
        super.dados();
        System.out.println("Setor: " + setor);
    }
}

public class empresa {
    private static void calculoSalario(double hora, double valorHora, int opcao) {
        double salario = hora * valorHora;
        
        if (opcao == 4 || opcao == 2) {
            salario *= 1.02; // Aumentar 2% para Gerentes e Diretores
        } else {
            salario *= 1.05; // Aumentar 5% para demais funcionários
        }

        System.out.println("O salario do funcionario é :" + salario);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe o tipo de funcionário:");
        System.out.println("1 - Engenheiro");
        System.out.println("2 - Diretor");
        System.out.println("3 - Secretário");
        System.out.println("4 - Gerente");
        int opcao = scanner.nextInt();
        scanner.nextLine(); // Consumir a nova linha

        System.out.println("Digite o código do funcionário:");
        String codigo = scanner.nextLine();
        System.out.println("Digite o nome do funcionário:");
        String nome = scanner.nextLine();
        System.out.println("Digite o sexo do funcionário:");
        String sexo = scanner.nextLine();
        System.out.println("Digite o número de horas trabalhadas:");
        int numeroDeHoras = scanner.nextInt();
        System.out.println("Digite o valor da hora trabalhada:");
        double valorHora = scanner.nextDouble();
        scanner.nextLine();

        switch (opcao) {
            case 1:
                System.out.println("Digite a especialidade do engenheiro:");
                String especialidade = scanner.nextLine();
                System.out.println("Digite o CREA do engenheiro:");
                String crea = scanner.nextLine();

                funcionario engenheiro = new Engenheiro(codigo, nome, sexo, numeroDeHoras, valorHora, especialidade, crea);
                engenheiro.dados();

                calculoSalario(numeroDeHoras, valorHora, opcao);
                break;
            case 2:
                System.out.println("Digite a área de gestão do diretor:");
                String areaGestao = scanner.nextLine();

                funcionario diretor = new Diretor(codigo, nome, sexo, numeroDeHoras, valorHora, areaGestao);
                diretor.dados();

                calculoSalario(numeroDeHoras, valorHora, opcao);
                break;
            case 3:
                System.out.println("Digite a categoria do Secretario");
                String categoria = scanner.nextLine();
                System.out.println("Digite o setor do secretario");
                String setor = scanner.nextLine();

                funcionario secretario = new Secretario(codigo, nome, sexo, numeroDeHoras, valorHora, categoria, setor);
                secretario.dados();

                calculoSalario(numeroDeHoras, valorHora, opcao);
                break;
            case 4:
                System.out.println("Digite o setor do gerente");
                String setorGerente = scanner.nextLine();

                funcionario gerente = new Gerente(codigo, nome, sexo, numeroDeHoras, valorHora, setorGerente);
                gerente.dados();

                calculoSalario(numeroDeHoras, valorHora, opcao);
                break;
            default:
                break;
        }

        scanner.close();
    }

}