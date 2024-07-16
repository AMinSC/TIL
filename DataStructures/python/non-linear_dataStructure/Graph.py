class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend([n for n in self.graph[node]
                              if n not in visited])

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for next in self.graph[start]:
            if next not in visited:
                self.dfs(next,visited)


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("BFS starting from vertex 2:")
    graph.bfs(2)

    print("\nDFS starting from vertex 2:")
    graph.dfs(2)