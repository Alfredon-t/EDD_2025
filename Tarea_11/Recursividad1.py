from Pila import Stack


def quitar_medio(stack, actual, medio):
    # Caso base: Si llegamos al índice medio
    if actual == medio:
        return stack.pop()

    # Desapilar el elemento actual
    top = stack.pop()

    # Recursión: continuar hacia el siguiente nivel
    valor_medio = quitar_medio(stack, actual + 1, medio)

    # Volver a apilar el elemento que se desapiló
    stack.push(top)

    return valor_medio

# Función principal que calcula el índice medio y llama a la función recursiva


def obtener_medio(stack):
    if stack.is_empty():
        return None  # Caso de pila vacía

    indice_medio = stack.length() // 2
    return quitar_medio(stack, 0, indice_medio)


def main():
    stack = Stack()

    # Pushing elements to the stack
    for i in range(1, 6):
        stack.push(i)

    print("Pila original:", stack)

    # Extracting the middle value
    valor_medio = obtener_medio(stack)
    print("Valor medio:", valor_medio)

    # Verifying the stack after extraction
    print("Pila después de sacar el valor medio:", stack)


if __name__ == "__main__":
    main()
