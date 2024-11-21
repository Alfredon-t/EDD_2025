class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __lt__(self, other):
        return self.id_producto < other.id_producto

    def __eq__(self, other):
        return self.id_producto == other.id_producto

    def __str__(self):
        return (f"ID: {self.id_producto}, Nombre: {self.nombre}, "
                f"Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}")
