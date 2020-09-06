class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        # We can print with list abilities, but only print!
        return str(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)