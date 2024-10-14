from Array2D import Array2d
from Pila import Stack
import pygame

pygame.init()

# Colores 
MURO = (0, 0, 0)  
PASILLO = (255, 255, 255)  
SERPIENTE = (10, 150, 20)  
ENTRADA = (255, 255, 0)
SALIDA = (255, 0, 0)
SIN_SALIDA = (192, 192, 192)

PANTALLA = 30  

class Laberinto:
    def __init__(self, tablero_laberinto):
        self.laberinto = Array2d(len(tablero_laberinto), len(tablero_laberinto[0]))
        self.stack = Stack()
        self.visitado = Array2d(len(tablero_laberinto), len(tablero_laberinto[0]))
        
        for r, row in enumerate(tablero_laberinto):
            for c, cell in enumerate(row):
                self.laberinto.set_item(r, c, cell)

        self.rows = len(tablero_laberinto)
        self.cols = len(tablero_laberinto[0])
        self.iniciar = (self.rows - 1, 0) #Inicio
        self.fin = ((self.rows // 2)-1, self.cols - 1)  #Salida
        self.stack.push(self.iniciar)
        self.encontro_salida = False

    def crear_laberinto(self, screen):
        while not self.encontro_salida and not self.stack.is_empty():
            pos_actual = self.stack.peek()
            row, col = pos_actual
            self.visitado.set_item(row, col, True)  #Visitado

            movimientos = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            se_movio = False

            for dir_fil, dir_col in movimientos:
                new_row, new_col = row + dir_fil, col + dir_col

                if (0 <= new_row < self.rows and 0 <= new_col < self.cols and
                    self.laberinto.get_item(new_row, new_col) in [' ', 'E'] and
                    not self.visitado.get_item(new_row, new_col)):
                    self.stack.push((new_row, new_col))
                    se_movio = True

                    #Comprobar salida
                    if self.laberinto.get_item(new_row, new_col) == 'E' or (new_row, new_col) == self.fin:
                        self.encontro_salida = True
                    break

            if not se_movio:
                quitar_pos_actual = self.stack.pop()  #Quitar la posición actual
                self.visitado.set_item(quitar_pos_actual[0], quitar_pos_actual[1], 'x')  #MArcar con gris que no tiene salida

            self.dibujar_laberinto(screen)
            pygame.time.delay(250)  #Velocidad

    def dibujar_laberinto(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                celda = self.laberinto.get_item(row, col)

                if (row, col) in self.stack.data: 
                    color = SERPIENTE  
                elif self.visitado.get_item(row, col) == 'x':  # 'x' para indicar que no tiene salida
                    color = SIN_SALIDA
                elif celda == ' ':  # ' ' para indicar un pasillo
                    color = PASILLO
                elif (row, col) == self.iniciar:
                    color = ENTRADA
                elif (row, col) == self.fin:
                    color = SALIDA
                else:
                    color = MURO

                pygame.draw.rect(screen, color,
                                 pygame.Rect(col * PANTALLA, row * PANTALLA, PANTALLA, PANTALLA))

        pygame.display.flip()

tablero_laberinto = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#'],
    ['#', ' ', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#'],
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', '#'],
    ['#', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' '],
    ['#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', 'E'],
    ['#', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
]



def main():
    laberinto = Laberinto(tablero_laberinto)

    tamanio_pantalla = (len(tablero_laberinto[0]) * PANTALLA, len(tablero_laberinto) * PANTALLA)
    pantalla = pygame.display.set_mode(tamanio_pantalla)
    pygame.display.set_caption("Laberinto EDD_2025")

    corriendo = True
    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

        laberinto.crear_laberinto(pantalla)

        if laberinto.encontro_salida:
            corriendo = False 

    pygame.quit()

if __name__ == "__main__":
    main()
