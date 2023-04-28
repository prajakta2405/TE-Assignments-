import heapq

def dijkstra(graph, start):
    """
    Compute the single-source shortest path for a weighted graph using Dijkstra's algorithm.
    graph: a dictionary of dictionaries representing the graph, with edge weights as values
    start: the starting vertex
    """
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    
    pq = [(0, start)]
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distances
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

start = 'A'
distances = dijkstra(graph, start)

print(f"Shortest distances from {start}: {distances}")
