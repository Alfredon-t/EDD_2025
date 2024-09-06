class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

    def get_dato(self):
        return self.dato

    def get_siguiente(self):
        return self.siguiente

    def set_dato(self, dato):
        self.dato = dato

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def __str__(self):
        return f"Nodo{{dato = {self.dato}, siguiente = {self.siguiente}}}"