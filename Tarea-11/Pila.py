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
        info = "\n-----\n"
        for elem in self.data[-1::-1]:
            info += f"{elem}\n---\n"
        return info
