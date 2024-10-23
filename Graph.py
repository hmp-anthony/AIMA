class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskal_mst(self):
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)

            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = find(parent, u)
            y = find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                union(parent, rank, x, y)

        return result

