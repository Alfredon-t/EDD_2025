class Stack():
    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.length() == 0

    def length(self):
        return len(self.data)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def push(self, value):
        self.data.append(value)

    def __str__(self):
        info = "-----"
        for elem in self.data[-1::-1]:
            print(elem, "\n---")


pila_ejem = Stack()
print("Esta vacía??", pila_ejem.is_empty())
print("long??", pila_ejem.length())
pila_ejem.push('a')
pila_ejem.push('b')
pila_ejem.push('c')
pila_ejem.__str__()
tmp = pila_ejem.peek()
print("El valor en el tope es: ", tmp)
print(".-.-.-.-.-")
pila_ejem.__str__()
print(".-.-.-POP.-.-.-.")
tmp2 = pila_ejem.pop()

print("El valor sacado con pop es: ", tmp2)
print("El nuevo estado de la pila es: ")
pila_ejem.__str__()
