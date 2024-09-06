package Listas;

import Nodos.Nodo;

public class ListaADTMain {
    public static void main(String[] args) {
        ListaLigada ll = new ListaLigada<>();
        ll.agregarAlFinal(11);
        ll.agregarAlFinal(22);
        ll.agregarAlFinal(33);
        ll.transversal();
        ll.estaVacia();
        ll.insertarAlInicio(5);
        ll.transversal();
        System.out.println(ll.getTamanio());

        Perro perro1 = new Perro("Poddle", 3, "Alberto");
        System.out.println(perro1);
        System.out.println("-.-.-.-.-.-");
        ListaLigada<Perro> perros = new ListaLigada<>();
        perros.agregarAlFinal(perro1);
        perros.transversal();
        System.out.println(".-.-.-.-");
        perros.agregarAlFinal(new Perro("Chihuahua", 4, "Keshi"));
        perros.transversal();

    }
}