class NodoArbol:
    def __init__(self, dato=None, hijo_izq=None, hijo_der=None):
        self.dato = dato
        self.hijo_izq = hijo_izq
        self.hijo_der = hijo_der

    def get_dato(self):
        return self.dato

    def set_dato(self, dato):
        self.dato = dato

    def get_hijo_izq(self):
        return self.hijo_izq

    def set_hijo_izq(self, hijo_izq):
        self.hijo_izq = hijo_izq

    def get_hijo_der(self):
        return self.hijo_der

    def set_hijo_der(self, hijo_derecho):
        self.hijo_der = hijo_derecho

    def __eq__(self, other):
        if isinstance(other, NodoArbol):
            return self.dato == other.dato
        return False

    def __hash__(self):
        return hash(self.dato)

    def __str__(self):
        return f"NodoArbol(dato={self.dato}, hijo_izquierdo={self.hijo_izq}, hijo_derecho={self.hijo_der})"
