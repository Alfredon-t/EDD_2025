class Array2d:
    def __init__(self, ren, col):
        self.rowSize = ren
        self.colSize = col
        self.data = [['' for _ in range(col)] for _ in range(ren)]

    def get_rowSize(self):
        return self.rowSize

    def get_colSize(self):
        return self.colSize

    def get_item(self, ren, col):
        if 0 <= ren < self.rowSize and 0 <= col < self.colSize:
            return self.data[ren][col]
        else:
            print("Índices fuera de rango.")

    def set_item(self, ren, col, dato):
        if 0 <= ren < self.rowSize and 0 <= col < self.colSize:
            self.data[ren][col] = dato
        else:
            print("Índices fuera de rango.")

    def clear(self, dato):
        for i in range(self.rowSize):
            for j in range(self.colSize):
                self.data[i][j] = dato

    def __str__(self):
        str_rep = ""
        for i in range(self.rowSize):
            for j in range(self.colSize):
                str_rep += f"{self.data[i][j]}, "
            str_rep += "\n"
        return str_rep
