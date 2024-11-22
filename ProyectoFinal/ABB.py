class Nodo:
    def __init__(self, producto):
        self.producto = producto  # Aquí usamos 'producto' en lugar de 'dato'
        self.izquierdo = None
        self.derecho = None


class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, producto):
        if self.raiz is None:
            self.raiz = Nodo(producto)
        else:
            self.ins_recursivo(self.raiz, producto)

    def ins_recursivo(self, nodo, producto):
        if producto.id_producto < nodo.producto.id_producto:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(producto)
            else:
                self.ins_recursivo(nodo.izquierdo, producto)
        elif producto.id_producto > nodo.producto.id_producto:
            if nodo.derecho is None:
                nodo.derecho = Nodo(producto)
            else:
                self.ins_recursivo(nodo.derecho, producto)
        else:
            nodo.producto.cantidad += producto.cantidad

    def buscar(self, id_producto):
        return self.bus_recursivo(self.raiz, id_producto)

    def bus_recursivo(self, nodo, id_producto):
        if nodo is None:
            return None
        if id_producto == nodo.producto.id_producto:
            return nodo.producto
        elif id_producto < nodo.producto.id_producto:
            return self.bus_recursivo(nodo.izquierdo, id_producto)
        else:
            return self.bus_recursivo(nodo.derecho, id_producto)

    def buscar_por_nombre(self, nombre):
        return self.bus_por_nombre(self.raiz, nombre)

    def bus_por_nombre(self, nodo, nombre):
        if nodo is None:
            return None
        if nodo.producto.nombre.lower() == nombre.lower():
            return nodo.producto
        encontrado_izq = self.bus_por_nombre(nodo.izquierdo, nombre)
        if encontrado_izq:
            return encontrado_izq
        return self.bus_por_nombre(nodo.derecho, nombre)

    def eliminar(self, id_producto, cantidad):
        self.raiz, eliminado = self.elim_recursivo(
            self.raiz, id_producto, cantidad)
        return eliminado

    def elim_recursivo(self, nodo, id_producto, cantidad):
        if nodo is None:
            return nodo, False

    def elim_recursivo(self, nodo, id_producto, cantidad):
        if nodo is None:
            return nodo, False

        eliminado = False
        if id_producto == nodo.producto.id_producto:
            if nodo.producto.cantidad >= cantidad:
                nodo.producto.cantidad -= cantidad
                if nodo.producto.cantidad == 0:
                    nodo = None
                eliminado = True
            else:
                print("Error: No hay suficiente cantidad para eliminar.")
        elif id_producto < nodo.producto.id_producto:
            nodo.izquierdo, eliminado = self.elim_recursivo(
                nodo.izquierdo, id_producto, cantidad)
        else:
            nodo.derecho, eliminado = self.elim_recursivo(
                nodo.derecho, id_producto, cantidad)
        return nodo, eliminado

    def encontrar_min(self, nodo):
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
            resultado.append(nodo.producto)
            self.in_orden_recursivo(nodo.derecho, resultado)
