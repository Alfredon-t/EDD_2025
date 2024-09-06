package Nodos;

public class Nodos27 {
    public static void main(String[] args) {
        Nodo<Integer> head = new Nodo<>();
        head.setDato(11);

        head.setSiguiente(new Nodo<>(22, new Nodo<>(33, null)));

        /*
         * Nodo<Integer> head2 = new Nodo<>(10, new Nodo<>(20, new Nodo<>(40, new
         * Nodo<>(50))));
         * 
         * head2.getSiguiente().setSiguiente(new Nodo<>(35,
         * head2.getSiguiente().getSiguiente()));
         * System.out.println(head2.getSiguiente().getSiguiente().getSiguiente().getDato
         * ());
         */

        head.getSiguiente().setSiguiente(new Nodo<>(29, head.getSiguiente().getSiguiente()));
        Nodo<Integer> aux = head;
        System.out.print("|");
        while (aux != null) {
            System.out.print(aux.getDato() + "| -> |");
            aux = aux.getSiguiente();
        }
        System.out.print("null|");

        System.out.println();

        Nodo<Integer> head2 = new Nodo<>(5, head);
        aux = head2;
        System.out.print("|");
        while (aux != null) {
            System.out.print(aux.getDato() + "| -> |");
            aux = aux.getSiguiente();
        }
        System.out.print("null|");

    }

}