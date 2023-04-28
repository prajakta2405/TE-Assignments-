import sys
from typing import List


V = 5

class MST:

   
    def minKey(self, key: List[int], mstSet: List[bool]) -> int:
        
        min = sys.maxsize
        min_index = -1

        for v in range(V):
            if not mstSet[v] and key[v] < min:
                min = key[v]
                min_index = v

        return min_index

    
    def printMST(self, parent: List[int], graph: List[List[int]]) -> None:
        print("Edge \tWeight")
        for i in range(1, V):
            print(parent[i], "-", i, "\t", graph[i][parent[i]])

   
    def primMST(self, graph: List[List[int]]) -> None:
       
        parent = [None] * V

        
        key = [sys.maxsize] * V

        mstSet = [False] * V

    
        for i in range(V):
            key[i] = sys.maxsize
            mstSet[i] = False

       
        key[0] = 0

      
        parent[0] = -1

        
        for count in range(V - 1):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

           
            for v in range(V):

               
                if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
                    parent[v] = u
                    key[v] = graph[u][v]

       
        self.printMST(parent, graph)


t = MST()
graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]


t.primMST(graph)
