from Array2D import Array2d
from Pila import Stack
import pygame

pygame.init()


MURO = (0, 0, 0)  
PASILLO = (255, 255, 255)  
SERPIENTE = (50, 100, 50)  
ENTRADA = (255, 255, 0)
SALIDA = (255, 0, 0)
SIN_SALIDA = (192, 192, 192)

PANTALLA = 30  

class Laberinto:
    def __init__(self, tablero_laberinto):
        self.laberinto = Array2d(len(tablero_laberinto), len(tablero_laberinto[0]))
        self.stack = Stack()
        self.visitado = Array2d(len(tablero_laberinto), len(tablero_laberinto[0]))
        
        # Cargar el laberinto estático
        for r, row in enumerate(tablero_laberinto):
            for c, cell in enumerate(row):
                self.laberinto.set_item(r, c, cell)

        self.rows = len(tablero_laberinto)
        self.cols = len(tablero_laberinto[0])
        self.start = (0, 0)  # La entrada
        self.end = (self.rows - 1, self.cols - 1)  # La salida
        self.stack.push(self.start)  # Inicializa la pila con la entrada
        self.found_exit = False  # Variable para saber si se encontró la salida

    def generate_maze(self, screen):
        """Genera el laberinto y mueve la serpiente hasta la salida"""
        while not self.found_exit and not self.stack.is_empty():
            current_pos = self.stack.peek()
            row, col = current_pos
            self.visitado.set_item(row, col, True)  # Marcar como visitado

            # Definimos las direcciones: Izquierda, Arriba, Derecha, Abajo
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Orden fijo

            found_move = False

            for d_row, d_col in directions:
                new_row, new_col = row + d_row, col + d_col

                # Verificamos si el movimiento es válido
                if (0 <= new_row < self.rows and 0 <= new_col < self.cols and
                    self.laberinto.get_item(new_row, new_col) in [' ', 'E'] and
                    not self.visitado.get_item(new_row, new_col)):
                    self.stack.push((new_row, new_col))  # Agregamos la nueva posición
                    found_move = True

                    # Verificamos si hemos llegado a la salida
                    if self.laberinto.get_item(new_row, new_col) == 'E':
                        self.found_exit = True
                    break

            if not found_move:
                # Si no hay movimientos válidos, retrocedemos
                dead_end_pos = self.stack.pop()  # Sacamos la posición actual
                # Pintamos la posición como SIN_SALIDA
                self.visitado.set_item(dead_end_pos[0], dead_end_pos[1], 'x')  # Marcar como sin salida

            # Mostrar el laberinto con la serpiente avanzando
            self.show_maze(screen)
            pygame.time.delay(300)  # Ajustamos el retraso para animación

    def show_maze(self, screen):
        """Dibuja el laberinto con la serpiente avanzando o retrocediendo"""
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.laberinto.get_item(row, col)

                if (row, col) in self.stack.data:  # El rastro de la serpiente
                    color = SERPIENTE  # Color verde para la serpiente
                elif self.visitado.get_item(row, col) == 'x':  # Caminos sin salida
                    color = SIN_SALIDA
                elif cell == ' ':  # Pasillos
                    color = PASILLO
                elif cell == 'S':  # Entrada
                    color = ENTRADA
                elif cell == 'E':  # Salida
                    color = SALIDA
                else:  # Paredes
                    color = MURO

                pygame.draw.rect(screen, color,
                                 pygame.Rect(col * PANTALLA, row * PANTALLA, PANTALLA, PANTALLA))

        pygame.display.flip()  # Actualizamos la pantalla


# Laberinto estático
maze_layout = [
    ['S', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' '],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', ' '],
    ['#', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' '],
    ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' '],
    ['#', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' '],
    ['#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' '],
    [' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' '],
    ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' '],
    [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', 'E', ' '],
    ['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]




def main():
    laberinto = Laberinto(maze_layout)

    # Configuramos la pantalla de pygame
    screen_size = (len(maze_layout[0]) * PANTALLA, len(maze_layout) * PANTALLA)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Laberinto Estático")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Generamos el laberinto con animación
        laberinto.generate_maze(screen)

        # Finaliza una vez que la serpiente ha llegado a la salida
        if laberinto.found_exit:
            running = False 

    pygame.quit()


if __name__ == "__main__":
    main()
