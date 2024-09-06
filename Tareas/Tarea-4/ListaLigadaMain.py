class SmartPhone:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"SmartPhone({self.marca}, {self.modelo}, ${self.precio})"


def main():
    from ListaLigada import ListaLigada
    lista = ListaLigada()

    lista.agregar_al_inicio(SmartPhone("Apple", "iPhone 15 pro", 34999))
    lista.agregar_después_de(lista.head.get_dato(), SmartPhone("Honor", "Magic 6 lite", 3070))
    lista.agregar_al_final(SmartPhone("Samsung", "Galaxy A55", 8400))
    lista.agregar_al_final(SmartPhone("Motorola", "Moto G84", 5545))
    lista.agregar_al_final(SmartPhone("Poco", "F6 pro", 9499))

    print("Contenido: ")
    lista.transversal()

    lista.eliminar(2)
    print("\nDespués de eliminar el Smartphone de la posición 2:")
    lista.transversal()

    nuevo_smartphone = SmartPhone("Samsung", "Galaxy A34", 7999)
    segundo_smartphone = lista.head.get_siguiente().get_dato()
    lista.actualizar(segundo_smartphone, nuevo_smartphone)
    print("\nSegundo elemento actualizado:")
    lista.transversal()

    lista.agregar_al_inicio(SmartPhone("Motorola", "Moto G04s", 2550))
    lista.agregar_al_final(SmartPhone("Apple", "iPhone 14 pro", 32999))
    print("\nNueva lista luego de agregar un elemento al inicio y otro al final:")
    lista.transversal()

    lista.eliminar_el_primero()
    print("\nDespués de eliminar el primer Smartphone:")
    lista.transversal()


if __name__ == "__main__":
    main()
