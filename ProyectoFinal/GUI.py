import tkinter as tk
from tkinter import messagebox
from ABB import ABB
from Producto import Producto


class App:
    def __init__(self, root):
        self.arbol = ABB()
        self.root = root
        self.root.title("Proyecto Final")
        self.root.geometry("600x400")  # Tamaño inicial
        self.root.resizable(True, True)  # Permitir redimensionar
        self.next_id = 1
        self.componentes()
        self.configurar_grid()

    def componentes(self):
        # Etiqueta principal
        self.titulo_label = tk.Label(
            self.root, text="Gestión de Inventario", font=("Arial", 16))
        self.titulo_label.grid(
            row=0, column=0, columnspan=2, pady=10, sticky="nsew")

        # Crear un frame para centrar los campos
        self.campos_frame = tk.Frame(self.root)
        self.campos_frame.grid(
            row=1, column=0, columnspan=2, pady=20, sticky="nsew")

        self.campos_frame.grid_columnconfigure(0, weight=1)
        self.campos_frame.grid_columnconfigure(1, weight=1)

        # Campos y etiquetas dentro del frame
        self.crear_fila("ID:", 0, "id_entry", self.campos_frame)
        self.crear_fila("Nombre:", 1, "nombre_entry", self.campos_frame)
        self.crear_fila("Precio:", 2, "precio_entry", self.campos_frame)
        self.crear_fila("Cantidad:", 3, "cantidad_entry", self.campos_frame)

        # Crear un frame para los botones
        self.botones_frame = tk.Frame(self.root)
        self.botones_frame.grid(
            row=2, column=0, columnspan=2, pady=20, sticky="nsew")

        self.botones_frame.grid_columnconfigure(0, weight=1)
        self.botones_frame.grid_columnconfigure(1, weight=1)

        # Botones con separación
        self.agregar_btn = tk.Button(
            self.botones_frame, text="Agregar", command=self.agregar)
        self.agregar_btn.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.eliminar_btn = tk.Button(
            self.botones_frame, text="Eliminar", command=self.eliminar)
        self.eliminar_btn.grid(row=0, column=1, padx=10,
                               pady=10, sticky="nsew")

        self.buscar_btn = tk.Button(
            self.botones_frame, text="Buscar", command=self.buscar)
        self.buscar_btn.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.listar_btn = tk.Button(
            self.botones_frame, text="Listar", command=self.listar)
        self.listar_btn.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    def crear_fila(self, texto, fila, entrada_nombre, parent):
        """Crea una fila con etiqueta y campo de entrada dentro de un parent frame."""
        etiqueta = tk.Label(parent, text=texto)
        etiqueta.grid(row=fila, column=0, sticky="e", padx=5, pady=5)
        entrada = tk.Entry(parent)
        entrada.grid(row=fila, column=1, sticky="nsew", padx=5, pady=5)
        setattr(self, entrada_nombre, entrada)

    def configurar_grid(self):
        """Configura el comportamiento del grid para expandirse."""
        # Configurar pesos para filas y columnas
        for i in range(7):  # Número de filas
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(2):  # Número de columnas
            self.root.grid_columnconfigure(j, weight=1)

    def agregar(self):
        try:
            # Obtener datos del formulario
            nombre = self.nombre_entry.get().strip()
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())

            # Validaciones
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            if precio <= 0:
                raise ValueError("El precio debe ser mayor a 0.")
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a 0.")

            # Verificar si el producto ya existe
            producto_existente = self.arbol.buscar_por_nombre(nombre)
            if producto_existente and producto_existente.precio == precio:
                producto_existente.cantidad += cantidad
                messagebox.showinfo(
                    "Éxito",
                    f"Producto ya existente. Cantidad actualizada: {
                        producto_existente.cantidad} unidades.",
                )
            elif producto_existente and producto_existente.precio != precio:
                raise ValueError(
                    f"Ya existe un producto con el nombre '{
                        nombre}' pero con un precio diferente."
                )
            else:
                # Crear nuevo producto
                producto = Producto(self.next_id, nombre, precio, cantidad)
                self.arbol.insertar(producto)
                self.next_id += 1
                messagebox.showinfo(
                    "Éxito", "Producto agregado correctamente.")

            self.limpiar()

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")

    def eliminar(self):
        # Obtener el ID y la cantidad desde los campos de entrada
        id_producto = self.id_entry.get()
        cantidad = self.cantidad_entry.get()

        # Verificar que el ID y la cantidad sean números válidos
        try:
            id_producto = int(id_producto)  # Convertir el ID a entero
        except ValueError:
            messagebox.showerror("Error", "ID no válido.")
            return

        try:
            cantidad = int(cantidad)  # Convertir la cantidad a entero
        except ValueError:
            messagebox.showerror("Error", "Cantidad no válida.")
            return

        # Llamar al método de eliminación con los parámetros ID y cantidad
        eliminado = self.arbol.eliminar(id_producto, cantidad)
        if eliminado:
            messagebox.showinfo("Éxito", f"Producto con ID {
                                id_producto} eliminado con éxito.")
        else:
            messagebox.showwarning(
                "Error", f"No se pudo eliminar el producto con ID {id_producto}.")

    def buscar(self):
        try:
            id_producto = int(self.id_entry.get())
            producto = self.arbol.buscar(id_producto)
            if producto:
                messagebox.showinfo("Producto encontrado", str(producto))
            else:
                messagebox.showwarning("Aviso", "Producto no encontrado.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un ID válido.")

    def listar(self):
        productos = self.arbol.in_orden()
        if productos:
            lista = "\n".join(str(producto) for producto in productos)
            messagebox.showinfo("Inventario", lista)
        else:
            messagebox.showinfo(
                "Inventario", "No hay productos en el inventario.")

    def limpiar(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
