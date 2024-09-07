import java.util.Arrays;

public class ColaConPrioridadAcotada<E> {
    private ColaADT<E>[] colas;
    private int maxPrioridad;

    public ColaConPrioridadAcotada(int maxPrioridad) {
        this.maxPrioridad = maxPrioridad;
        this.colas = new ColaADT[maxPrioridad];
        for (int i = 0; i < this.maxPrioridad + 1; i++) {
            this.colas[i] = new ColaADT<>();
        }
    }

    public int longitud() {
        int total = 0;
        for (int i = 0; i < maxPrioridad + 1; i++) {
            total += this.colas[i].longitud();
        }
        return total;
    }

    public boolean estaVacia() {
        return this.longitud() == 0;
    }

    public void encolar(int prioridad, E elemento) {
        if (prioridad >= 1 && prioridad <= this.maxPrioridad + 1) {
            this.colas[prioridad].encolar(elemento);
        }
    }

    public void desEncolar(int prioridad, E elemento) {
        if (this.estaVacia()) {
            System.out.println("No hay mas elementos");
        } else {
            /*
             * while (condition) {
             * 
             * }
             */
        }
    }

    @Override
    public String toString() {
        return "ColaConPrioridadAcotada [colas=" + Arrays.toString(colas) + ", maxPrioridad=" + maxPrioridad + "]";
    }

}
