from ConjuntoADT import ConjuntoADT

if __name__ == "__main__":
    conjunto1 = ConjuntoADT()  # 1, 4, 5, 14, 24, 38, 47, 88
    conjunto2 = ConjuntoADT()  # 2, 3, 4, 5, 14, 23, 38, 47, 89

    conjunto1.agregar(3, 7, 12, 21, 0, 6, 9)
    conjunto2.agregar(2, 5, 10, 16, 9, 25, 8)

    print(f"Conjunto 1: {conjunto1.conjunto}")
    print(f"Conjunto 2: {conjunto2.conjunto}")
    print("")

    print("Longitud de los conjuntos:")
    print(f"Conjunto 1: {conjunto1.longitud()}")
    print(f"Conjunto 2: {conjunto2.longitud()}")
    print("")

    print("Comprobación de pertenencia de un elemento")
    print(f"El conjunto 1 contiene '10': {conjunto1.contiene(10)}")
    print(f"El conjunto 2 contiene '10': {conjunto2.contiene(10)}")
    print("")

    print("Eliminación de elementos ")
    conjunto2.eliminar(10)
    print(f"El conjunto 2 contiene '10' después de la eliminación: {
          conjunto2.contiene(10)}")
    print("")

    print("Unión de conjuntos")
    union = conjunto1.union(conjunto2)
    print(f"Unión del conjunto 1 y 2: {union.conjunto}")
    print("")

    print("Intersección de conjuntos")
    interseccion = conjunto1.interseccion(conjunto2)
    print(f"Intersección del conjunto 1 y 2: {interseccion.conjunto}")
    print("")

    print("Diferencia de conjuntos")
    diferencia = conjunto1.diferencia(conjunto2)
    print(f"Diferencia del conjunto 1 y 2: {diferencia.conjunto}")
    print("")

    print("Comprobación de subconjuntos")
    print(f"El conjunto 1 es subconjunto de 2: {
          conjunto1.esSubConjunto(conjunto2)}")
    print(f"La intersección entre los conjuntos es subconjunto del conjunto 2: {
          interseccion.esSubConjunto(conjunto2)}")
    print("")

    print("Uso de equals")
    print(f"El conjunto 1 es igual al conjunto 2: {
          conjunto1.equals(conjunto2)}")
