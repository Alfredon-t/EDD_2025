from JuegoDeLaVida import JuegoDeLaVida


class Main:
    def run():
        rows, cols = 11, 11
        juego = JuegoDeLaVida(rows, cols)

        iniciar = [(4, 5),
                   (5, 4), (5, 5), (5, 6),
                   (6, 4), (6, 6),
                   (7, 5)]
        juego.set_iniciar(iniciar)

        juego.play(8)


if __name__ == "__main__":
    Main.run()
