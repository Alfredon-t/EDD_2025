import tkinter as tk
from tkinter import messagebox
from ABB import ABB
from Producto import Producto


class App:
    def __init__(self, root):
        self.inventario = ABB()
        self.root = root
        self.root.title("Proyecto Final")

        self.create_widgets()

    def create_widgets(self):
        # Títulos
        tk.Label(self.root, text="Gestión de Inventario", font=(
            "Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Campos para el producto
        tk.Label(self.root, text="ID:").grid(row=1, column=0, sticky="e")
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Nombre:").grid(row=2, column=0, sticky="e")
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Precio:").grid(row=3, column=0, sticky="e")
        self.precio_entry = tk.Entry(self.root)
        self.precio_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Cantidad:").grid(row=4, column=0, sticky="e")
        self.cantidad_entry = tk.Entry(self.root)
        self.cantidad_entry.grid(row=4, column=1)

        # Botones
        tk.Button(self.root, text="Agregar", command=self.agregar_producto).grid(
            row=5, column=0, pady=10)
        tk.Button(self.root, text="Eliminar",
                  command=self.eliminar_producto).grid(row=5, column=1)
        tk.Button(self.root, text="Buscar",
                  command=self.buscar_producto).grid(row=6, column=0)
        tk.Button(self.root, text="Listar",
                  command=self.listar_inventario).grid(row=6, column=1)

    def agregar_producto(self):
        try:
            id_producto = int(self.id_entry.get())
            nombre = self.nombre_entry.get()
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
            producto = Producto(id_producto, nombre, precio, cantidad)
            self.inventario.insertar(producto)
            messagebox.showinfo("Éxito", "Producto agregado correctamente.")
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Ingrese datos válidos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_producto(self):
        try:
            id_producto = int(self.id_entry.get())
            eliminado = self.inventario.eliminar(Producto(id_producto))
            if eliminado:
                messagebox.showinfo(
                    "Éxito", "Producto eliminado correctamente.")
            else:
                messagebox.showwarning("Aviso", "Producto no encontrado.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un ID válido.")

    def buscar_producto(self):
        try:
            id_producto = int(self.id_entry.get())
            producto = self.inventario.buscar(Producto(id_producto))
            if producto:
                messagebox.showinfo("Producto encontrado", str(producto))
            else:
                messagebox.showwarning("Aviso", "Producto no encontrado.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un ID válido.")

    def listar_inventario(self):
        productos = self.inventario.in_orden()
        if productos:
            lista = "\n".join(str(producto) for producto in productos)
            messagebox.showinfo("Inventario", lista)
        else:
            messagebox.showinfo(
                "Inventario", "No hay productos en el inventario.")

    def limpiar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
