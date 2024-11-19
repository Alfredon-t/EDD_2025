class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, elemento):
        if self.raiz is None:
            self.raiz = Nodo(elemento)
        else:
            self.ins_recurivo(self.raiz, elemento)

    def ins_recurivo(self, nodo, elemento):
        if elemento < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(elemento)
            else:
                self.ins_recurivo(nodo.izquierdo, elemento)
        elif elemento > nodo.dato:
            if nodo.derecho is None:
                nodo.derecho = Nodo(elemento)
            else:
                self.ins_recurivo(nodo.derecho, elemento)
        else:
            raise ValueError("Elemento con ID duplicado no permitido.")

    def buscar(self, elemento):
        return self.bus_recursivo(self.raiz, elemento)

    def bus_recursivo(self, nodo, elemento):
        if nodo is None:
            return None
        if elemento == nodo.dato:
            return nodo.dato
        elif elemento < nodo.dato:
            return self.bus_recursivo(nodo.izquierdo, elemento)
        else:
            return self.bus_recursivo(nodo.derecho, elemento)

    def eliminar(self, elemento):
        self.raiz, eliminado = self.elim_recursivo(self.raiz, elemento)
        return eliminado

    def elim_recursivo(self, nodo, elemento):
        if nodo is None:
            return nodo, False

        eliminado = False
        if elemento == nodo.dato:
            eliminado = True
            if nodo.izquierdo and nodo.derecho:
                sucesor = self.minimo(nodo.derecho)
                nodo.dato = sucesor.dato
                nodo.derecho, _ = self.elim_recursivo(
                    nodo.derecho, sucesor.dato)
            else:
                nodo = nodo.izquierdo if nodo.izquierdo else nodo.derecho
        elif elemento < nodo.dato:
            nodo.izquierdo, eliminado = self.elim_recursivo(
                nodo.izquierdo, elemento)
        else:
            nodo.derecho, eliminado = self.elim_recursivo(
                nodo.derecho, elemento)

        return nodo, eliminado

    def minimo(self, nodo):
        while nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo

    def in_orden(self):
        resultado = []
        self.in_orden_recursivo(self.raiz, resultado)
        return resultado

    def in_orden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self.in_orden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self.in_orden_recursivo(nodo.derecho, resultado)
