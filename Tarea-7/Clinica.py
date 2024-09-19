from ColasADT import Queue


class Paciente:
    def __init__(self, nombre, edad, sintoma):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma

    def __str__(self):
        return f"Nombre: {self.nombre}\t\tEdad: {self.edad}\tSintomas: {self.sintoma}"


def main():
    cola_pacientes = Queue()

    paciente1 = Paciente("Aaron", 21, "Dolor de estómago")
    paciente2 = Paciente("Martha", 19, "Migraña")
    paciente3 = Paciente("Martín", 40, "Cuerpo cortado")

    cola_pacientes.encolar(paciente1)
    cola_pacientes.encolar(paciente2)
    cola_pacientes.encolar(paciente3)

    print("Se agregaron 3 nuevos pacientes: ")
    print(cola_pacientes)

    print("\nEl proxímo paciente a atender es: ")
    print(cola_pacientes.frente())

    print("\nSe esta atendiento al paciente...")
    cola_pacientes.des_encolar()

    print("\nLa cola después de atender al paciente es: ")
    print(cola_pacientes)

    paciente4 = Paciente("Laura", 22, "Diarrea")
    paciente5 = Paciente("Fabian", 12, "Dolor en la garganta")

    cola_pacientes.encolar(paciente4)
    cola_pacientes.encolar(paciente5)

    print("\nSe esta atendiendo al paciente...")
    cola_pacientes.des_encolar()

    print("\nLa cola después de atender al paciente es: ")
    print(cola_pacientes)


if __name__ == "__main__":
    main()
