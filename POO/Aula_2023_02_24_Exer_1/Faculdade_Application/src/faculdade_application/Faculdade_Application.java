
package faculdade_application;
import java.util.Scanner;
import org.me.faculdade.Faculdade_Class;
public class Faculdade_Application {

    public static void main(String[] args) {
        
        Faculdade_Class f1  = new Faculdade_Class();
        
        Scanner leia = new Scanner(System.in);
        String nome;
        String curso;
        int ra;
        double nota;
        double mensalidade;
   
        System.out.print("Informe o Nome: ");
        nome = leia.nextLine();
        System.out.print("Informe o Curso: ");
        curso = leia.nextLine();
        System.out.print("Informe o RA: ");
        ra = leia.nextInt();
        System.out.print("Informe a Nota: ");
        nota = leia.nextDouble();
        System.out.print("Informe a Mensalidade: ");
        mensalidade = leia.nextDouble();
    
         //alterando os atributos
        f1.setNome(nome);
        f1.setCurso(curso);
        f1.setRA(ra);
        f1.setNota(nota);
        f1.setMensalidade(mensalidade);
    
        //retornando os valores
        System.out.println("Nome: " + f1.getNome());
        System.out.println("Curso: "  + f1.getCurso());
        System.out.println("RA: " + f1.getRA());
        System.out.println("Nota: " + f1.getNota());
        System.out.println("Mensalidade " + f1.getMensalidade());
        System.out.printf("Desconto %.2f \n",f1.calculaDesconto(mensalidade));
    
    }
    
}
