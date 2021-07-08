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

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        shortest_paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
                        if shortest_path not in shortest_paths and shortest_paths == []:
                            shortest_paths.append(shortest_path)
                        else:
                            for sps in shortest_paths:
                                if len(sps) < len(shortest_path):
                                    continue
                                else:
                                    shortest_paths.remove(sps)
                                    shortest_paths.append(shortest_path)

        return shortest_path

    def bfs(self, src):
        dist = {}
        q = Queue()
        q.enqueue(src)
        visited = []
        visited.append(src)
        dist[src] = 0

        while not q.is_empty():
            top = q.front()
            print(top)
            q.dequeue()

            if top in self.graph_dict:
                for node in self.graph_dict[top]:
                    if node not in visited:
                        q.enqueue(node)
                        visited.append(node)
                        dist[node] = dist[top] + 1

        print(dist)


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
    route_graph.bfs('Mumbai')
    print("----------------")
    route_graph.bfs('Dubai')