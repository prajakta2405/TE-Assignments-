import heapq

def dijkstra(graph, start):
   
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    visited = set()
    heap = [(0, start)]
    
    while heap:
        (distance, vertex) = heapq.heappop(heap)
        if vertex not in visited:
            visited.add(vertex)
            for neighbor, weight in graph[vertex].items():
                dist = distance + weight
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(heap, (dist, neighbor))
    
    return distances
graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3, 'D': 2, 'E': 1},
    'C': {'B': 3, 'E': 1},
    'D': {'A': 1, 'B': 2, 'E': 4},
    'E': {'B': 1, 'C': 1, 'D': 4}
}

start = 'A'
distances = dijkstra(graph, start)

print("Shortest paths:")
for vertex, distance in distances.items():
    print(f"Vertex: {vertex}, Distance: {distance}")

