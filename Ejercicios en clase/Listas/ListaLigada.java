package Listas;

import Nodos.Nodo;

public class ListaLigada<T> {
    private Nodo<T> head;
    private int tamanio;

    public ListaLigada() {
    }

    public void agregarAlFinal(T dato) {
        Nodo<T> nuevo = new Nodo<>(dato);
        if (head == null) {
            head = nuevo;
        } else {
            Nodo<T> aux = this.head;
            while (aux.getSiguiente() != null) {
                aux = aux.getSiguiente();
            }
            aux.setSiguiente(nuevo);
        }

    }

    public void transversal() {
        Nodo<T> aux = this.head;
        while (aux != null) {
            System.out.print(aux.getDato() + " --> ");
            aux = aux.getSiguiente();
        }
        System.out.println("");
    }

    public boolean estaVacia() {

        if (this.head == null) {

            System.out.println("esta vacia");
            return true;

        }

        System.out.println("no esta vacia");

        return false;

    }

    public void insertarAlInicio(T dato) {

        this.head = new Nodo<>(dato, this.head);

    }

    public int getTamanio() {
        Nodo aux = this.head;
        int contador = 0;
        while (aux != null) {
            contador++;
            aux = aux.getSiguiente();

        }
        return contador;

    }

}