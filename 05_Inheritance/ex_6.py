class Stack:
    def __init__(self, *args):
        self.data = [str(el) for el in args]

    def push(self, el):
        self.data.append(str(el))

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"
