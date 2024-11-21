import tkinter as tk
from tkinter import messagebox
from ABB import ABB
from Producto import Producto


class App:
    def __init__(self, root):
        self.inventario = ABB()
        self.root = root
        self.root.title("Proyecto Final")
        self.root.geometry("600x400")  # Tamaño inicial
        self.root.resizable(True, True)  # Permitir redimensionar
        self.id_contador = 1
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
            producto_existente = self.inventario.buscar_por_nombre(nombre)
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
                self.inventario.insertar(producto)
                self.next_id += 1
                messagebox.showinfo(
                    "Éxito", "Producto agregado correctamente.")

            self.limpiar()

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")

    def eliminar(self):
        try:
            # Obtener datos del formulario
            id_producto = int(self.id_entry.get())
            cantidad_eliminar = int(self.cantidad_entry.get())

            # Validaciones
            if cantidad_eliminar <= 0:
                raise ValueError("La cantidad a eliminar debe ser mayor a 0.")

            # Buscar el producto en el inventario
            producto_existente = self.inventario.buscar(
                Producto(id_producto, "", 0, 0))
            if producto_existente:
                if producto_existente.cantidad > cantidad_eliminar:
                    producto_existente.cantidad -= cantidad_eliminar
                    messagebox.showinfo(
                        "Éxito",
                        f"Se eliminaron {cantidad_eliminar} unidades. Quedan {
                            producto_existente.cantidad} unidades.",
                    )
                elif producto_existente.cantidad == cantidad_eliminar:
                    self.inventario.eliminar(producto_existente)
                    messagebox.showinfo(
                        "Éxito", "Producto eliminado completamente.")
                else:
                    messagebox.showwarning(
                        "Aviso",
                        "No hay suficientes unidades para eliminar la cantidad especificada.",
                    )
            else:
                messagebox.showwarning("Aviso", "Producto no encontrado.")

            self.limpiar()

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")

    def buscar(self):
        try:
            id_producto = int(self.id_entry.get())
            producto = self.inventario.buscar(id_producto)
            if producto:
                messagebox.showinfo("Producto encontrado", str(producto))
            else:
                messagebox.showwarning("Aviso", "Producto no encontrado.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un ID válido.")

    def buscar_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def listar(self):
        productos = self.inventario.in_orden()
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
