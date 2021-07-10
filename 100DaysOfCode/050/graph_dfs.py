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

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)



if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Paris", "Mumbai"),
        ("Mumbai", "Dubai"),
        ("Dubai", "Mumbai"),
        ("Paris", "Dubai"),
        ("Dubai", "Paris"),
        ("Paris", "New York"),
        ("New York", "Paris"),
        ("Dubai", "New York"),
        ("New York", "Dubai"),
        ("New York", "Toronto"),
        ("Toronto", "New York")
    ]

    route_graph = Graph(routes)