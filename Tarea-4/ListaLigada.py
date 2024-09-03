from Nodo import Nodo
class ListaLigada():
    def __init__(self):
        self.head = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.head is None

    def get_tamanio(self):
        return self.tamanio

    def agregar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.get_siguiente = self.head
        self.head = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.head = nuevo_nodo
        else: 
            actual = self.head
            while actual.get_siguiente() != None:
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo_nodo)
        self.tamanio += 1

    def agregar_después_de(self,referencia,valor):
        aux = self.head
        while aux and aux.get_dato != referencia:
            aux = aux.get_siguiente
        if aux:
            nuevo_nodo = Nodo(valor)
            nuevo_nodo.get_siguiente = aux.get_siguiente
            aux.get_siguiente = nuevo_nodo
            self.tamanio += 1

    def eliminar(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("La posición no existe")
        aux = self.head
        if posicion == 0:
            self.head = aux.get_siguiente
        else:
            previo = None
            for _ in range(posicion):
                previo = aux
                aux = aux.get_siguiente
            previo.get_siguiente = aux.get_siguiente
        self.tamanio -= 1

    def eliminar_el_primero(self):
        if not self.esta_vacia():
            self.head = self.head.get_siguiente
            self.tamanio -= 1

    def eliminar_el_final(self):
        if self.esta_vacia():
            return
        aux = self.head
        if aux.get_siguiente is None:
            self.head = None
        else:
            previo = None
            while aux.get_siguiente:
                previo = aux
                aux = aux.get_siguiente
            previo.get_siguiente = None
        self.tamanio -= 1

    def buscar(self, valor):
        aux = self.head
        posicion = 0
        while aux:
            if aux.get_dato == valor:
                return posicion
            aux = aux.get_siguiente
            posicion += 1
        return "No se pudo encontrar el valor"

    def actualizar(self, a_buscar, valor):
        aux = self.head
        while aux:
            if aux.get_dato == a_buscar:
                aux.get_dato = valor
                return True
            aux = aux.get_siguiente
        return False

    def transversal(self):
        aux = self.head
        items = []
        while aux:
            items.append(aux.get_dato)
            aux = aux.get_siguiente
        print(" -> ".join(map(str, items)))