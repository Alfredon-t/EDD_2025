import tkinter as tk
from tkinter import messagebox
from ABB import ABB
from Producto import Producto


class Interfaz:
    def __init__(self, principal):
        self.arbol = ABB()
        self.principal = principal
        self.principal.title("Proyecto Final EDD_2025")
        self.principal.geometry("500x400")
        self.principal.resizable(True, True)
        self.sig_id = 1
        self.componentes()
        self.config_grid()

    def componentes(self):
        self.titulo_lb = tk.Label(
            self.principal, text="Sistema de Inventario", font=("Arial", 16))
        self.titulo_lb.grid(
            row=0, column=0, columnspan=2, pady=10, sticky="nsew")

        self.campos_pos = tk.Frame(self.principal)
        self.campos_pos.grid(
            row=1, column=0, columnspan=2, pady=20, sticky="nsew")

        self.campos_pos.grid_columnconfigure(0, weight=1)
        self.campos_pos.grid_columnconfigure(1, weight=1)

        self.fila("ID:", 0, "id_entry", self.campos_pos)
        self.fila("Nombre:", 1, "nombre_entry", self.campos_pos)
        self.fila("Precio:", 2, "precio_entry", self.campos_pos)
        self.fila("Cantidad:", 3, "cantidad_entry", self.campos_pos)

        self.botones_pos = tk.Frame(self.principal)
        self.botones_pos.grid(
            row=2, column=0, columnspan=2, pady=20, sticky="nsew")

        self.botones_pos.grid_columnconfigure(0, weight=1)
        self.botones_pos.grid_columnconfigure(1, weight=1)

        self.agregar_btn = tk.Button(
            self.botones_pos, text="Agregar", command=self.agregar)
        self.agregar_btn.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.eliminar_btn = tk.Button(
            self.botones_pos, text="Eliminar", command=self.eliminar)
        self.eliminar_btn.grid(row=0, column=1, padx=10,
                               pady=10, sticky="nsew")

        self.buscar_btn = tk.Button(
            self.botones_pos, text="Buscar", command=self.buscar)
        self.buscar_btn.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.listar_btn = tk.Button(
            self.botones_pos, text="Listar", command=self.listar)
        self.listar_btn.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    def fila(self, texto, fila, entrada_nombre, parent):
        etiqueta = tk.Label(parent, text=texto)
        etiqueta.grid(row=fila, column=0, sticky="e", padx=5, pady=5)
        entrada = tk.Entry(parent)
        entrada.grid(row=fila, column=1, sticky="nsew", padx=5, pady=5)
        setattr(self, entrada_nombre, entrada)

    def config_grid(self):
        for i in range(7):
            self.principal.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.principal.grid_columnconfigure(j, weight=1)

    def agregar(self):
        try:
            nombre = self.nombre_entry.get().strip()
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())

            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            if precio <= 0:
                raise ValueError("El precio debe ser mayor a 0.")
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a 0.")

            producto_exis = self.arbol.buscar_por_nombre(nombre)
            if producto_exis and producto_exis.precio == precio:
                producto_exis.cantidad += cantidad
                messagebox.showinfo(
                    "Proyecto Final",
                    f"El producto ya existe, se ha actualizado su cantidad: {
                        producto_exis.cantidad} unidades.",
                )
            elif producto_exis and producto_exis.precio != precio:
                raise ValueError(
                    f"El producto '{
                        nombre}' existe, pero con un precio diferente."
                )
            else:
                producto = Producto(self.sig_id, nombre, precio, cantidad)
                self.arbol.insertar(producto)
                self.sig_id += 1
                messagebox.showinfo(
                    "Proyecto Final", "El producto se agrego correctamente.")

            self.limpiar()

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def eliminar(self):
        id_producto = self.id_entry.get()
        cantidad = self.cantidad_entry.get()

        try:
            id_producto = int(id_producto)
        except ValueError:
            messagebox.showerror("Error", "No existe el ID.")
            return

        try:
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror(
                "Error", "La cantidad ingresada no es válida.")
            return

        eliminado = self.arbol.eliminar(id_producto, cantidad)
        if eliminado:
            messagebox.showinfo("Proyecto Final", f"El producto con ID {
                                id_producto} ha sido eliminado con éxito.")
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
                messagebox.showwarning(
                    "Aviso", "El producto no ha sido encontrado.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un ID válido.")

    def listar(self):
        productos = self.arbol.in_orden()
        if productos:
            lista = "\n".join(str(producto) for producto in productos)
            messagebox.showinfo("Inventario", lista)
        else:
            messagebox.showinfo(
                "Inventario", "El inventario esta vacío.")

    def limpiar(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)


if __name__ == "__main__":
    principal = tk.Tk()
    gui = Interfaz(principal)
    principal.mainloop()
