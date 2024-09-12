from Array2D import Array2d


class JuegoDeLaVida:
    def __init__(self, row, col):
        self.tablero = Array2d(row, col)
        self.rows = row
        self.cols = col
        self.tablero.clear('x')  # 'x' es una célula muerta

    def get_vecinos_vivos(self, row, col):
        direcciones = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1), (0, 1),
                       (1, -1), (1, 0), (1, 1)]
        vecinos_vivos = 0

        for d in direcciones:
            new_row, new_col = row + d[0], col + d[1]
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if self.tablero.get_item(new_row, new_col) == '0':
                    vecinos_vivos += 1

        return vecinos_vivos

    def set_iniciar(self, celulas_vivas):
        for celula in celulas_vivas:
            # '0' es una célula viva
            self.tablero.set_item(celula[0], celula[1], '0')

    def siguiente_gen(self):
        new_tablero = Array2d(self.rows, self.cols)
        new_tablero.clear('x')

        for i in range(self.rows):
            for j in range(self.cols):
                vecinos_vivos = self.get_vecinos_vivos(i, j)
                celula_actual = self.tablero.get_item(i, j)

                if celula_actual == '0':
                    if vecinos_vivos == 2 or vecinos_vivos == 3:
                        new_tablero.set_item(i, j, '0')
                    else:
                        new_tablero.set_item(i, j, 'x')
                else:
                    if vecinos_vivos == 3:
                        new_tablero.set_item(i, j, '0')
                    else:
                        new_tablero.set_item(i, j, 'x')
        self.tablero = new_tablero

    def play(self, generaciones):
        for gen in range(generaciones):
            print(f"Generacion {gen + 1}")
            print(self.tablero)
            self.siguiente_gen
