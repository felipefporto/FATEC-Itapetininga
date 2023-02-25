
package inss_application1;
import java.util.Scanner;
import java.util.Set;
import org.me.inss.INSS_Class;
public class INSS_Application1 {

    public static void main(String[] args) {
        INSS_Class i1 = new INSS_Class();
        Scanner leia = new Scanner(System.in);
        
        String nome;
        int cpf;
        String email;
        double salario_bruto;
        
        System.out.print("Informe o nome: ");
        nome = leia.nextLine();
        System.out.print("Informe o CPF: ");
        cpf = leia.nextInt();
        System.out.print("Informe o email: ");
        email = leia.next();
        System.out.print("Informe o Salário Bruto: ");
        salario_bruto = leia.nextDouble();
        
        i1.setNome(nome);
        i1.setCPF(cpf);
        i1.setEmail(email);
        i1.setSalarioBruto(salario_bruto);
        
        System.out.println("Nome: " + i1.getNome());
        System.out.println("CPF: "  + i1.getCPF());
        System.out.println("Email: " + i1.getEmail());
        System.out.printf("INSS: %.2f\n",i1.calculaINSS(salario_bruto));
        System.out.printf("Salário Líquido: %.2f \n",i1.calculaSalario_Liquido(salario_bruto));
    }
    
}
