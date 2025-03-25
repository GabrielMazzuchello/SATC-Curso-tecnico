package aula06;
import javax.swing.JOptionPane;

public class Ex15 {
    
    public static void main(String[] args){
        funcionarios();
    }

    public static void funcionarios(){
        double Tvenda, Tcompras, Tproducao, Tfinanceiro, Tincorreto, SalarioMin, SalarioMax, SalarioT;
        SalarioMin = 999999;
        SalarioMax = 0;
        Tvenda = 0;
        Tcompras = 0;
        Tproducao = 0;
        Tfinanceiro = 0;
        Tincorreto = 0;
        SalarioT = 0;

        for (int i = 0; i < 3; i++) {

            String nome = JOptionPane.showInputDialog("Nome:  ");
            String setor = JOptionPane.showInputDialog("Setor:\nV- Vendas\nC- Compras\nP- Produção\nF- Financeiro  ");
            double salario = Double.parseDouble(JOptionPane.showInputDialog("Salário:  "));

            if (setor.equalsIgnoreCase("v")) {
                Tvenda = Tvenda + 1;
            }
            else if (setor.equalsIgnoreCase("c")) {
                Tcompras = Tcompras + 1;
            }
            else if (setor.equalsIgnoreCase("p")) {
                Tproducao = Tproducao + 1;
            }
            else if (setor.equalsIgnoreCase("f")) {
               Tfinanceiro = Tfinanceiro + 1; 
            }
            else {
                JOptionPane.showMessageDialog(null, "Valor inválido");
                Tincorreto = Tincorreto + 1;
            }

            if (salario > 1) {
                if (salario > SalarioMax) {
                    SalarioMax = salario;
                }
                if (SalarioMin > salario) {
                    SalarioMin = salario;
                }
                SalarioT = SalarioT + salario;
            }
            else {
                JOptionPane.showMessageDialog(null, "Valor inválido");
            }
        }

        JOptionPane.showMessageDialog(null, "Total de funcionários por setor\nVenda: "+Tvenda+"\nCompras: "+Tcompras+"\nProdução: "+Tproducao+"\nFinanceiro: "+Tfinanceiro+"\nInválido: "+Tincorreto, "Funcionários por setor", 0);
        JOptionPane.showMessageDialog(null, "Salário máximo: " + SalarioMax + "\nSalário mínimo: " + SalarioMin, "Salários", 0);
        JOptionPane.showMessageDialog(null, "Salário total: " + SalarioT, "Salário total", 0);
    }
}