package Nodos;

public class DoubleLinkedList<T> {
    private NodoDoble<T> head;
    private NodoDoble<T> tail;
    private int tamanio;

    public DoubleLinkedList() {
    }

    public boolean estaVacia() {
        boolean res = false;
        if (this.head == null && this.tail == null) {
            res = true;
        }
        return res;
    }

    public int getTamanio() {
        return tamanio;
    }

    public void agregarAlInicio(T valor) {
        NodoDoble<T> nuevo = new NodoDoble<>();
        if (this.estaVacia()) {
            this.head = nuevo;
            this.tail = nuevo;
        } else {
            this.head.setAnterior(nuevo);
            nuevo.setSiguiente(this.head);
            this.head = nuevo;
        }
        this.tamanio++;
    }

    // si es 0 de izq a der si es 1 de der a izq
    public void transversal(int direccion) {
        if (direccion == 1) {
            NodoDoble<T> aux = this.tail;
            while (aux != null) {
                System.out.print(aux);
                aux = aux.getAnterior();
            }
        } else if (direccion != 1) {
            NodoDoble<T> aux = this.head;
            while (aux != null) {
                System.out.print(aux);
                aux = aux.getSiguiente();
            }
        }
        System.out.println("");
    }

    public void agregarDespuesDe(T referencia, T valor) {
        NodoDoble<T> aux = this.head;
        while (aux.getDato() != referencia) {
            aux = aux.getSiguiente();
        }
        if (aux == null) {
            System.out.println("No existe la referencia");
        } else {
            // Hago el cambio
            // crear nuevo nodo
        }
}
