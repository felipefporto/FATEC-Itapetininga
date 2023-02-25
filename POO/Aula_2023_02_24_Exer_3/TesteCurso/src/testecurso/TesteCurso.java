
package testecurso;
import org.me.curso.Curso;
public class TesteCurso {

    public static void main(String[] args) {
        // TODO code application logic here
        Curso c1 = new Curso("Inglês", 8, 100.00);
        System.out.println("Curso: " + c1.getNome());
        System.out.println("Duração: " + c1.getDuracao());
        System.out.println("Valor: " + c1.getValor());
        
    }
    
}
