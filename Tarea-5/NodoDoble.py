class NodoDoble:
    def __init__(self, value, siguiente=None, anterior=None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, value):
        self.data = value

    def set_next(self, siguiente):
        self.next = siguiente

    def set_prev(self, anterior):
        self.prev = anterior

    def __str__(self):
        return f"<--|{self.data}|-->"
