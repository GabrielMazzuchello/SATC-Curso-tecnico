public class Desenvolvedor extends Funcionario {
    String linguagem;

    Desenvolvedor(String nome, double salario, String linguagem) {
        super(nome, salario);
        this.linguagem = linguagem;
    }

    public void exibirInfo() {
        super.exibirInfo();
        System.out.println("Linguagem: "+ linguagem);
    }
    
}
