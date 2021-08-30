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

    def front(self):
        if not self.is_empty():
            return self.container[-1]


def binary_numbers(n):
    queue = Queue()
    queue.enqueue("1")

    for i in range(n):
        front = queue.front()
        print(" ", front)
        queue.enqueue(front + "0")
        queue.enqueue(front + "1")

        queue.dequeue()


if __name__ == '__main__':
    binary_numbers(20)