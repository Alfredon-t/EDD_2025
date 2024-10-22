from NodoArbol import NodoArbol


class ArbolMain:
    def crear_arbol_numeros(self):
        # Creamos los nodos del árbol de números
        nodo_1 = NodoArbol(1)
        nodo_5 = NodoArbol(5, hijo_izq=nodo_1)
        nodo_25 = NodoArbol(25)
        nodo_15 = NodoArbol(15, hijo_der=nodo_25)
        nodo_10 = NodoArbol(10, hijo_izq=nodo_5, hijo_der=nodo_15)

        return nodo_10  # Este es el nodo raíz

    def crear_arbol_nombres(self):
        # Creamos los nodos del árbol de nombres
        nodo_susan = NodoArbol("Susan")
        nodo_diana = NodoArbol("Diana")
        nodo_pedro = NodoArbol(
            "Pedro", hijo_izq=nodo_susan, hijo_der=nodo_diana)
        nodo_mario = NodoArbol("Mario")
        nodo_diego = NodoArbol(
            "Diego", hijo_izq=nodo_pedro, hijo_der=nodo_mario)
        return nodo_diego  # Este es el nodo raíz


def main():
    # Crear una instancia de ArbolMain
    arbol_main = ArbolMain()

    # Crear el árbol de números
    arbol_numeros = arbol_main.crear_arbol_numeros()  # Llamada al método de instancia
    print("Árbol de números:")
    print(arbol_numeros)

    # Crear el árbol de nombres
    arbol_nombres = arbol_main.crear_arbol_nombres()  # Llamada al método de instancia
    print("\nÁrbol de nombres:")
    print(arbol_nombres)


if __name__ == "__main__":
    main()
