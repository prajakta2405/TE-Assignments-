
def dfs(graph, visited, vertex):

    visited[vertex] = True
    print(vertex, end=' ')
    
   
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)
            

def dfs_full(graph):
   
    visited = [False] * len(graph)
    
   
    for vertex in range(len(graph)):
        if not visited[vertex]:
            dfs(graph, visited, vertex)


graph = [[1, 2], [0, 3, 4], [0, 4], [1, 4], [1, 2, 3]]


dfs_full(graph)
