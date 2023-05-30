import heapq


class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class A2:
    def __init__(self, adjac_lis):
        self.adj = adjac_lis
        self.H = {
            "A": 11,
            "B": 6,
            "C": 99,
            "D": 1,
            "E": 7,
            "G": 0
        }

    def get_neighbors(self, vertex):
        return self.adj[vertex]

    def h(self, v):
        return self.H[v]

    def a_star_algorithm(self, s, d):
        open_list = [(0, s)]  # priority queue (f, vertex)
        closed_list = set()

        g = {s: 0}  # current distances from start_node to all other nodes
        parent = {s: s}  # adjacency map of all nodes

        while open_list:
            _, n = heapq.heappop(open_list)

            if n == d:
                reconst_path = []
                while parent[n] != n:
                    reconst_path.append(n)
                    n = parent[n]
                reconst_path.append(n)
                reconst_path.reverse()
                print("Path found:", reconst_path)
                return

            if n in closed_list:
                continue

            closed_list.add(n)

            for v in self.get_neighbors(n):
                if v.vertex not in closed_list and v.vertex not in [vertex for _, vertex in open_list]:
                    heapq.heappush(open_list, (g[n] + v.weight + self.h(v.vertex), v.vertex))
                    parent[v.vertex] = n
                    g[v.vertex] = g[n] + v.weight

                elif g[v.vertex] > g[n] + v.weight:
                    parent[v.vertex] = n
                    g[v.vertex] = g[n] + v.weight

                    if v.vertex in closed_list:
                        closed_list.remove(v.vertex)
                        heapq.heappush(open_list, (g[v.vertex] + self.h(v.vertex), v.vertex))

        print("Path does not exist!")


adjac_lis = {
    "A": [Node("B", 2), Node("E", 3)],
    "B": [Node("C", 1), Node("G", 9)],
    "C": None,
    "D": [Node("G", 1)],
    "E": [Node("D", 6)]
}

graph = A2(adjac_lis)
graph.a_star_algorithm("A", "G")
