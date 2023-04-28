import heapq

def prim(graph, start):
   
    mst = set()  # set of edges in the Minimum Spanning Tree
    visited = set([start])
    edges = [
        (weight, start, neighbor)
        for neighbor, weight in graph[start].items()
    ]
    heapq.heapify(edges)
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.add((u, v, weight))
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, v, neighbor))
    
    return mst
graph = {
    'A': {'B': 2, 'D': 7},
    'B': {'A': 2, 'C': 3, 'D': 8, 'E': 5},
    'C': {'B': 3, 'E': 6},
    'D': {'A': 7, 'B': 8, 'E': 9, 'F': 4},
    'E': {'B': 5, 'C': 6, 'D': 9, 'F': 1},
    'F': {'D': 4, 'E': 1}
}

start = 'A'
mst = prim(graph, start)

print("Minimum Spanning Tree:")
for edge in mst:
    print(f"Edge: ({edge[0]}, {edge[1]}), Weight: {edge[2]}")
