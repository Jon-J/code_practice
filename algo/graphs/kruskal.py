class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    def add_edges(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_MST(self):
        result = []

        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.v):
            parent.append(node)
            rank.append(0)
        
        while e < self.v - 1:
            u,v,w = self.graph[i]

            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            print("{} -- {}".format(x,y))
            if x != y:
                e += 1
                result.append([u,v,w])
                self.union(parent, rank, x, y)

        print("Following are the edges in the constructed MST:")
        for u,v,w in result:
            print("{} -- {} == {}".format(u,v,w))

if __name__ == '__main__':
    g = Graph(4)
    g.add_edges(0, 1, 10)
    g.add_edges(0, 2, 6)
    g.add_edges(0, 3, 5)
    g.add_edges(1, 3, 15)
    g.add_edges(2, 3, 4)

    g.kruskal_MST()
