from Pila import Stack


class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def pop(self):
        return self.data.pop() if not self.is_empty() else None

    def push(self, value):
        self.data.append(value)


class Balance:
    def __init__(self):
        self.caracter = []

    def balanceo(self, txt):
        pila = Stack()
        apertura = {'(': ')', '{': '}'}
        cierre = {')': '(', '}': '{'}

        for car in txt:
            self.caracter.append(car)
            if car in apertura:
                pila.push(car)
            elif car in cierre:
                if pila.is_empty() or pila.pop() != cierre[car]:
                    return False
        return pila.is_empty()

    def main(self):
        txt = input("Ingrese un texto a verificar: ")
        if self.balanceo(txt):
            print("El texto está balanceado.")
        else:
            print("El texto no está balanceado.")


if __name__ == "__main__":
    verificar_bal = Balance()
    verificar_bal.main()
