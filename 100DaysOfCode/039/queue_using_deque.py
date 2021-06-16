from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, data):
        self.container.appendleft(data)

    def dequeue(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.container)
