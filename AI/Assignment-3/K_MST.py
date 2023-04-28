class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

def kruskal(graph):
    n = len(graph)
    edges = [(graph[i][j], i, j) for i in range(n) for j in range(i+1, n)]
    edges.sort()
    mst = set()
    dsu = DisjointSet(n)
    for w, u, v in edges:
        if dsu.union(u, v):
            mst.add((u, v, w))
    return mst
# Example graph represented as a 2D list
graph = [    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Compute minimum spanning tree using Kruskal's algorithm
mst = kruskal(graph)

# Output minimum spanning tree
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge[0], "-", edge[1], ":", edge[2])
