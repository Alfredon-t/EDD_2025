public class ProbarQueue {
    public static void main(String[] args) {
        ColaADT<Character> letras = new ColaADT<>();
        letras.encolar('A');
        letras.encolar('B');
        letras.encolar('C');
        letras.encolar('D');

        System.out.println(letras);
        System.out.println(letras.frente());
        System.out.println(letras);
        System.out.println("Atender: " + letras.desEncolar());
        System.out.println(letras);
        System.out.println("tam actual: " + letras.longitud());

    }
}