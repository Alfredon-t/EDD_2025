from Pila import Stack


def quitar_medio(stack, actual, medio):
    if actual == medio:
        return stack.pop()
    top = stack.pop()
    valor_medio = quitar_medio(stack, actual + 1, medio)
    stack.push(top)
    return valor_medio


def obtener_medio(stack):
    if stack.is_empty():
        return None

    indice_medio = stack.length() // 2
    return quitar_medio(stack, 0, indice_medio)


def main():
    stack = Stack()

    for i in range(1, 10):
        stack.push(i)
    print("Pila inicial:", stack)
    valor_medio = obtener_medio(stack)
    print("Valor medio:", valor_medio)
    print("Pila después de quitar el valor medio:", stack)


if __name__ == "__main__":
    main()
