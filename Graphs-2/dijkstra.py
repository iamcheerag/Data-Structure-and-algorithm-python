import sys
class graph:
    
    def _init_(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [ [ 0 for i in range(nVertices)] for j in range(nVertices)]
        
    def addEdge(self,v1,v2,wt):

        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt
                    
    def __getMinVertexD(self,visited,weight):
        minVertex = -1
        for i in range(self.nVertices):
            if(visited[i] is False and (minVertex == -1 or (weight[minVertex] > weight[i]))):
                minVertex = i
        return minVertex
    
    def djikstra(self):
        
        visited = [False for i in range(self.nVertices)]
        dist = [sys.maxsize for i in range(self.nVertices)]
        dist[0] = 0
        for i in range(self.nVertices - 1):
            minVertex = self.__getMinVertexD(visited,dist)
            visited[minVertex] = True
            
            for j in range(self.nVertices):
                if (self.adjMatrix[minVertex][j] > 0 and visited[j] is False):
                    if(dist[j] > dist[minVertex] + self.adjMatrix[minVertex][j]):
                        dist[j] = dist[minVertex] + self.adjMatrix[minVertex][j]
                        
        for i in range(self.nVertices):
            print(str(i) + " " + str(dist[i]))
    
vert,edges = list(map(int,input().split()))

g = graph()
for i in range(edges):
    inputArray = [int(i) for i in input().split()]
    g.addEdge(inputArray[0],inputArray[1],inputArray[2])

g.djikstra()