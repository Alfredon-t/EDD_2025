import LinkedList;

public class ColaADT<E>{
    private LinkedList<E> data;

    public ColaADT(){
        this.data = new LinkedList<>();
    }

    public LinkedList<E> getData(E data){
        return data;
    }

    public boolean  estaVacia(){
        boolean res = false;
        if(this.data.size() == 0){
            res = true;
        }
        return res;
    }   

    public int longitud(){
        return this.data.size();
    }

    public E frente(){
        return this.data.getFirst();
    }

    public void encolar(E valor){ //enqueue
        this.data.addLast(valor);
    }

    public E desEncolar(){
        return this.data.removeFirst();
    }

    @java.lang.Override
    public java.lang.String toString() {
        return "ColaADT{" +
                "data=" + data +
                '}';
    }
}