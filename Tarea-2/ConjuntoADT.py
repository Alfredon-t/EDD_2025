class ConjuntoADT():
    def __init__(self):
        self.conjunto = set()

    def longitud(self):
        return len(self.conjunto)

    def contiene(self, item):
        return item in self.conjunto

    def agregar(self, *items):
        self.conjunto.update(items)

    def eliminar(self, item):
        if self.contiene(item):
            self.conjunto.remove(item)

    def equals(self, otroConjunto):
        return self.conjunto == otroConjunto

    def esSubConjunto(self, otroConjunto):
        return self.conjunto.issubset(otroConjunto.conjunto)

    def union(self, otroConjunto):
        nuevoConjunto = ConjuntoADT()
        nuevoConjunto.conjunto = self.conjunto.union(otroConjunto.conjunto)
        return nuevoConjunto

    def interseccion(self, otroConjunto):
        nuevoConjunto = ConjuntoADT()
        nuevoConjunto.conjunto = self.conjunto.intersection(
            otroConjunto.conjunto)
        return nuevoConjunto

    def diferencia(self, otroConjunto):
        nuevoConjunto = ConjuntoADT()
        nuevoConjunto.conjunto = self.conjunto.difference(
            otroConjunto.conjunto)
        return nuevoConjunto
