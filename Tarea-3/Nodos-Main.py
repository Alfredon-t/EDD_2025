from Nodo import Nodo


class NodosMain:

    def imprimir(Nodo):
        aux = Nodo
        print("|", end="")
        while aux is not None:
            print(f"{aux.get_dato()}| -> |", end="")
            aux = aux.get_siguiente()
        print("null|")

    head = Nodo()
    head.set_dato(100)

    head.set_siguiente(Nodo(200, Nodo(300, Nodo(400, Nodo(600, None)))))
    imprimir(head)

    print("\nCambiar el nodo 300 a 333")
    head.get_siguiente().get_siguiente().set_dato(333)
    imprimir(head)

    print("\nAñadir el nodo 700 al final")
    head.get_siguiente().get_siguiente().get_siguiente(
    ).get_siguiente().set_siguiente(Nodo(700, None))
    imprimir(head)

    print("\nAñadir el nodo 50 al inicio")
    head = Nodo(50, head)
    imprimir(head)
