package Arrreglos;

public class array2dMain {
    public static void main(String[] args) {
        Array2d rejilla = new Array2d(6, 6);
        System.out.println(rejilla);
        rejilla.clear('0');
        System.out.println(rejilla);
        rejilla.setItem(1, 1, 'M');
        System.out.println(rejilla);
        System.out.println(rejilla.getItem(1, 1));
        System.out.println(rejilla.getItem(10, 1));
    }
}
