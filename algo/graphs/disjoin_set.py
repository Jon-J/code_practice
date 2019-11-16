from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.edges = defaultdict(list)

    def add_edges(self, u, v):
        self.edges[u].append(v)

class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

def find_parent(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find_parent(subsets, subsets[node].parent)
    return subsets[node].parent

def union(subsets, u, v):
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[u].rank < subsets[v].rank:
        subsets[u].parent = v
    else:
        subsets[v].parent = u
        subsets[u].rank += 1

def is_cycle(graph):
    subsets = []

    for u in range(graph.v):
        subsets.append(Subset(u, 0))

    for u in graph.edges:
        u_parent = find_parent(subsets, u)
        for v in graph.edges[u]:
            v_parent = find_parent(subsets, v)

            if v_parent == u_parent:
                return True
            else:
                union(subsets, u, v)
    return False

if __name__ == '__main__':
    # Driver Code
    g = Graph(3)

    # add edge 0-1
    g.add_edges(0, 1)

    # add edge 1-2
    g.add_edges(1, 2)

    # add edge 0-2
    g.add_edges(0, 2)

    if is_cycle(g):
        print('Graph contains cycle')
    else:
        print('Graph does not contain cycle')


        
