from ColaConPrioridadAcotada import ColaConPrioridadAcotada


class ClienteBanco:
    def __init__(self, nombre, perfil):
        self.nombre = nombre
        self.perfil = perfil

    def __str__(self):
        return f"{self.nombre} ({self.perfil})"


def main():
    banco = ColaConPrioridadAcotada(5)

    banco.encolar(4, ClienteBanco("Arturo", "Cliente Nuevo"))
    banco.encolar(4, ClienteBanco("Ximena", "Cliente Nuevo"))

    banco.encolar(5, ClienteBanco("Ernensto", "No es cliente"))
    banco.encolar(5, ClienteBanco("Blanca", "No es cliente"))
    banco.encolar(5, ClienteBanco("Ramón", "No es cliente"))

    banco.encolar(1, ClienteBanco("Luis Miguel", "Celebridad"))

    print("\nEstado de la cola:")
    print(banco)

    cliente_atendido = banco.des_encolar()
    print(f"\nAtendiendo a: {cliente_atendido}")
    print(f"{cliente_atendido.nombre} retiró $10,000 de su cuenta")

    banco.encolar(3, ClienteBanco("Marcos", "Cliente Frecuente"))
    banco.encolar(2, ClienteBanco("Sofía", "Cliente Premium"))

    cliente_atendido = banco.des_encolar()
    print(f"\nAtendiendo a: {cliente_atendido}")

    print("\nEstado de la cola:")
    print(banco)

    print("\nSe esta atendiendo a todos los clientes restantes:")
    while not banco.esta_vacia():
        cliente_atendido = banco.des_encolar()
        print(f"Atendiendo a: {cliente_atendido}")

    print("\nEstado final de la cola:")
    print(banco)


if __name__ == "__main__":
    main()
