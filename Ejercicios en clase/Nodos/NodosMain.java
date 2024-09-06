package Nodos;

public class NodosMain {
    public static void main(String[] args) {
        Nodo<Integer> head = new Nodo<>();
        head.setDato(10);

        // Nodo<Integer> nuevo = new Nodo<>();
        // nuevo.setDato(20);
        // head.setSiguiente(nuevo);

        // head.setSiguiente(new Nodo<>(20));
        head.setSiguiente(new Nodo<>(20, null));

        Nodo<Integer> head2 = new Nodo<>(10, new Nodo<>(20, new Nodo<>(40, new Nodo<>(50))));
        

        head2.getSiguiente().setSiguiente(new Nodo<>(35, head2.getSiguiente().getSiguiente()));
        System.out.println(head2.getSiguiente().getSiguiente().getSiguiente().getDato());

        Nodo<Integer> aux = head2;
        System.out.print("|");
        while (aux != null) {
            System.out.print(aux.getDato() + "| -> |");
            aux = aux.getSiguiente();
        }
        System.out.print("null|");

    }
}