class Queue:
    def __init__(self):
        self.data = []

    def est_vacia(self):
        return len(self.data) == 0

    def longitud(self):
        return len(self.data)

    def frente(self):
        if self.est_vacia():
            raise IndexError("La cola está vacía")
        return self.data[0]

    def encolar(self, valor):
        self.data.append(valor)

    def des_encolar(self):
        if self.est_vacia():
            raise IndexError("La cola está vacía")
        return self.data.pop(0)

    def __str__(self):
        return f"ColaADT(data={self.data})"
