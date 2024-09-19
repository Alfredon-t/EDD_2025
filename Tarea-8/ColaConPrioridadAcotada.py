from ColasADT import Queue


class ColaConPrioridadAcotada:
    def __init__(self, max_prioridad):
        self.max_prioridad = max_prioridad
        self.colas = [Queue() for _ in range(max_prioridad + 1)]

    def longitud(self):
        total = 0
        for cola in self.colas:
            total += cola.longitud()
        return total

    def esta_vacia(self):
        return self.longitud() == 0

    def encolar(self, prioridad, elemento):
        if 1 <= prioridad <= self.max_prioridad:
            self.colas[prioridad].encolar(elemento)

    def des_encolar(self):
        if self.esta_vacia():
            print("No hay más elementos")
        else:
            for cola in self.colas:
                if not cola.est_vacia():
                    return cola.des_encolar()
        return None

    def __str__(self):
        return f"ColaConPrioridadAcotada(colas={self.colas}, max_prioridad={self.max_prioridad})"
