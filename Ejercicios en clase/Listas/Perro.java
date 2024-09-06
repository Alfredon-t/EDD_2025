package Listas;

import Nodos.Nodo;

public class Perro {
    private String raza;
    private int edad;
    private String nombre;

    public Perro() {
    }

    public Perro(String raza, int edad, String nombre) {
        this.raza = raza;
        this.edad = edad;
        this.nombre = nombre;
    }

    public String getRaza() {
        return raza;
    }

    public void setRaza(String raza) {
        this.raza = raza;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "[ " +
                "raza='" + raza + '\'' +
                ", edad=" + edad +
                ", nombre='" + nombre + '\'' +
                ']';
    }
}