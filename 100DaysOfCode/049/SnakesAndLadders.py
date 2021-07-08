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

    def bfs(self, src, dest):
        dist = {}
        parent = {}
        q = Queue()
        q.enqueue(src)
        visited = []
        visited.append(src)
        dist[src] = 0
        parent[src] = -1

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
                        parent[node] = top

        print(dist)
        temp = dest
        while temp != -1:
            print(temp, "<--", end="")
            temp = parent[temp]

if __name__ == "__main__":
    board = {key: 0 for key in range(1,51)}
    board[2] = 13
    board[5] = 2
    board[9] = 18
    board[18] = 11
    board[17] = -13
    board[20] = -14
    board[24] = -8
    board[25] = -10
    board[32] = -2
    board[34] = -22

    edges = []
    for u in range(36):
        for dice in range(1,7):
            v = u + dice + board[u+dice]
            edges.append((u,v))

    graph = Graph(edges)
    graph.bfs(0, 36)