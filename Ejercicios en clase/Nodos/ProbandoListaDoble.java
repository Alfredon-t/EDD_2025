package Nodos;

public class ProbandoListaDoble {
    public static void main(String[] args) {
        DoubleLinkedList<Integer> numeros = new DoubleLinkedList<>();
        numeros.agregarAlInicio(10);
        if (numeros.estaVacia()) {
            System.out.println("Esta vacia");
        } else {
            System.out.println("No esta vacia");
        }

        numeros.transversal(0);
        numeros.agregarAlInicio(5);
        numeros.agregarAlInicio(4);
        numeros.agregarAlInicio(3);
        numeros.agregarAlInicio(2);
        numeros.agregarAlInicio(1);
        numeros.transversal(0);
        numeros.agregarDespuesDe(5);
    }
}
