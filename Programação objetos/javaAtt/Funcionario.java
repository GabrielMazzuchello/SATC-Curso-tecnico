public class Funcionario {
    String nome;
    double salario;

    Funcionario(String nome, double salario) {
        this.nome = nome;
        this.salario = salario;
    }

    public void exibirInfo() {
        System.out.println("Nome: "+ nome);
        System.out.println("Salario: "+ salario);
    }
}
