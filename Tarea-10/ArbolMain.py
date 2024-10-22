from NodoArbol import NodoArbol


class ArbolMain:
    def arbol_numeros(self):
        nodo1 = NodoArbol(1)
        nodo2 = NodoArbol(5, hijo_izq=nodo1)
        nodo3 = NodoArbol(25)
        nodo4 = NodoArbol(15, hijo_der=nodo3)
        raiz = NodoArbol(10, hijo_izq=nodo2, hijo_der=nodo4)
        return raiz

    def arbol_nombres(self):
        nodo1 = NodoArbol("Susan")
        nodo2 = NodoArbol("Diana")
        nodo3 = NodoArbol(
            "Pedro", hijo_izq=nodo1, hijo_der=nodo2)
        nodo4 = NodoArbol("Mario")
        raiz = NodoArbol(
            "Diego", hijo_izq=nodo3, hijo_der=nodo4)
        return raiz


def main():
    arbol_main = ArbolMain()

    arbol_numeros = arbol_main.arbol_numeros()
    print("Árbol de números:")
    print(arbol_numeros)

    arbol_nombres = arbol_main.arbol_nombres()
    print("\nÁrbol de nombres:")
    print(arbol_nombres)


if __name__ == "__main__":
    main()
