from collections import defaultdict
from queue import Queue
class graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)


    def BFS(self,s):
        output=[]
        queue=Queue()
        visited=[False]*(max(self.graph)+1)
           
           
        queue.put(s)
        visited[s]=True
        
        
        while not queue.empty():
            s=queue.get()
            output.append(s)
            for z in self.graph[s]:
                if visited[z]==False:
                    visited[z]=True
                    queue.put(z)
        print(output)

g=graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)
g.addedge(3,3)
g.BFS(2)