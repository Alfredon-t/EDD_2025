import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class EjemplosSets {

    public static List<Integer> eliminarDuplicados(List<Integer> listaOriginal){
        Set<Integer> conjunto = new HashSet<>();
        for (Integer item: listaOriginal) {
            conjunto.add(item)
        }
    }return conjunto.stream().toList();

}

public static void main(String[] args) {
    System.out.println("Ejemplo de sets");
    List<Integer> = listaConDuplicados = List.of(1,2,3,4,5,6,6,7,8,8,9);
}
