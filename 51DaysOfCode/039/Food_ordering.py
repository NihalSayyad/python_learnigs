import threading
import time

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

queue = Queue()
def place_order(orders):
    for item in orders:
        print(f"Pacing order for {item}")
        queue.enqueue(item)
        time.sleep(0.5)

def serve_order():
    while not queue.is_empty():
        print(f"Order served {queue.dequeue()}")
        time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']
t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order)

t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()
