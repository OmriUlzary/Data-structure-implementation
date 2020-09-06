class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        # We can print with list abilities, but only print!
        return str(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[self.size()-1]
