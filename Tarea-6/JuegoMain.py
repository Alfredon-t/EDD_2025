from JuegoDeLaVida import JuegoDeLaVida


class Main:
    def run():
        rows, cols = 5, 5
        juego = JuegoDeLaVida(rows, cols)

        iniciar = [(1, 2), (2, 2), (3, 2)]
        juego.set_iniciar(iniciar)

        juego.play(5)


if __name__ == "__main__":
    Main.run()
