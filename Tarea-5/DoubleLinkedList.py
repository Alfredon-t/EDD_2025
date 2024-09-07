from NodoDoble import NodoDoble


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.head is None

    def get_tamanio(self):
        return self.tamanio

    def agregar_al_inicio(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.esta_vacia():
            self.head = self.tail = nuevo_nodo
        else:
            nuevo_nodo.set_next(self.head)
            self.head.set_prev(nuevo_nodo)
            self.head = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.esta_vacia():
            self.head = self.tail = nuevo_nodo
        else:
            nuevo_nodo.set_prev(self.tail)
            self.tail.set_next(nuevo_nodo)
            self.tail = nuevo_nodo
        self.tamanio += 1

    def agregar_despues_de(self, referencia, valor):
        if self.esta_vacia():
            raise Exception("La lista está vacía.")
        nodo_actual = self.head
        while nodo_actual is not None and nodo_actual.get_data() != referencia:
            nodo_actual = nodo_actual.get_next()
        if nodo_actual is None:
            raise Exception("No se pudo encontrar la referencia.")
        nuevo_nodo = NodoDoble(valor)
        nuevo_nodo.set_next(nodo_actual.get_next())
        nuevo_nodo.set_prev(nodo_actual)
        if nodo_actual.get_next() is not None:
            nodo_actual.get_next().set_prev(nuevo_nodo)
        else:
            self.tail = nuevo_nodo
        nodo_actual.set_next(nuevo_nodo)
        self.tamanio += 1

    def obtener(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición fuera de rango.")
        nodo_actual = self.head
        for _ in range(posicion):
            nodo_actual = nodo_actual.get_next()
        return nodo_actual.get_data()

    def eliminar_el_primero(self):
        if self.esta_vacia():
            raise Exception("La lista está vacía.")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.get_next()
            self.head.set_prev(None)
        self.tamanio -= 1

    def eliminar_el_final(self):
        if self.esta_vacia():
            raise Exception("La lista está vacía.")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        self.tamanio -= 1

    def eliminar(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición fuera de rango.")
        if posicion == 0:
            self.eliminar_el_primero()
        elif posicion == self.tamanio - 1:
            self.eliminar_el_final()
        else:
            nodo_actual = self.head
            for _ in range(posicion):
                nodo_actual = nodo_actual.get_next()
            nodo_actual.get_prev().set_next(nodo_actual.get_next())
            nodo_actual.get_next().set_prev(nodo_actual.get_prev())
            self.tamanio -= 1

    def buscar(self, valor):
        nodo_actual = self.head
        posicion = 0
        while nodo_actual is not None:
            if nodo_actual.get_data() == valor:
                return posicion
            nodo_actual = nodo_actual.get_next()
            posicion += 1
        return -1

    def actualizar(self, valor_a_buscar, nuevo_valor):
        nodo_actual = self.head
        while nodo_actual:
            if nodo_actual.get_data() == valor_a_buscar:
                nodo_actual.set_data(nuevo_valor)
                return True
            nodo_actual = nodo_actual.get_next()
        return False

    def transversal(self, direccion='izquierda'):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        if direccion == 'izquierda':
            nodo_actual = self.head
            while nodo_actual is not None:
                print(nodo_actual, end=" <-> " if nodo_actual.get_next() else "\n")
                nodo_actual = nodo_actual.get_next()
        elif direccion == 'derecha':
            nodo_actual = self.tail
            while nodo_actual is not None:
                print(nodo_actual, end=" <-> " if nodo_actual.get_prev() else "\n")
                nodo_actual = nodo_actual.get_prev()
        else:
            raise ValueError(
                "La dirección no es valida.")
