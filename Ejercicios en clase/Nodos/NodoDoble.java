package Nodos;

public class NodoDoble<T> {
    private T dato;
    private NodoDoble<T> siguiente;
    private NodoDoble<T> anterior;

    public NodoDoble() {

    }

    public NodoDoble(T dato) {
        this.dato = dato;
    }

    public T getDato() {
        return dato;
    }

    public void setDato(T dato) {
        this.dato = dato;
    }

    public NodoDoble<T> getSiguiente() {
        return siguiente;
    }

    public void setSiguiente(NodoDoble<T> siguiente) {
        this.siguiente = siguiente;
    }

    public NodoDoble<T> getAnterior() {
        return anterior;
    }

    public void setAnterior(NodoDoble<T> anterior) {
        this.anterior = anterior;
    }

    @Override
    public String toString() {
        return "NodoDoble [dato=" + dato + ", siguiente=" + siguiente + ", anterior=" + anterior + "]";
    }
}
