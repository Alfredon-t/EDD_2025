package Arrreglos;

public class JuegoDeLaVida {
    private Array2d tablero;
    private Array2d tableroSiguienteGen;
    private int tamanio;

    public JuegoDeLaVida() {
    }

    public JuegoDeLaVida(Array2d tablero, int tamanio) {
        this.tablero = tablero;
        this.tamanio = tamanio;
    }

    public void aplicarReglas (){
        int vv = 0;
        //aplicar las 4 reglas
        for (int i = 0; i this.tamanio < ; i++) {
            for (int j = 0; j < this.tamanio; j++) {
                //aplicar la regla 1
                vv = numerosVecinosVivos(i, j)
            }
            
        }
    }

    public int numerosVecinosVivos(int ren, int row) {
        int vecinosVivos;
        // calcular el numero de vecinos vivos
        return vecinosVivos;
    }

}
