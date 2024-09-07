class DoubleLinkedListMain:
    def main():
        from DoubleLinkedList import DoubleLinkedList
        lista = DoubleLinkedList()

        lista.agregar_al_inicio(50)

        lista.agregar_al_final(60)
        lista.agregar_al_final(65)
        lista.agregar_al_final(70)
        lista.agregar_al_final(80)
        lista.agregar_al_final(90)

        print("Contenido inicial de la lista:")
        lista.transversal('izquierda')

        print("Contenido después de eliminar el tercer elemento:")
        lista.transversal('izquierda')

        lista.actualizar(lista.obtener(3), 88)

        print("Contenido de la lista después de actualizar el cuarto elemento:")
        lista.transversal('izquierda')

        posicion = lista.buscar(80)
        if posicion != -1:
            print(f"\nEl valor 80 se encuentra en la posición: {posicion}")
        else:
            print("\nEl valor 80 no se encuentra en la lista.")

    if __name__ == "__main__":
        main()
