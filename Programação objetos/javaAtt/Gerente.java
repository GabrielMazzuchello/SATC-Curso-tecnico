public class Gerente extends Funcionario {
    String departamento;

    Gerente(String nome, double salario, String departamento)  {
        super(nome, salario);
        this.departamento = departamento;
    }

    public void exibirInfo() {
        super.exibirInfo();
        System.out.println("Departamento: "+ departamento);
    }
}
