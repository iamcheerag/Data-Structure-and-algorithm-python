## Read input as specified in the question.
## Print output as specified in the question.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:36:27 2020

@author: Cheerag
"""

import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(nVertices)] for i in range(nVertices)]
        
    def addPath(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
    def getPathBfsHelper(self,v1,v2):
        visitedArray = [False for i in range(self.nVertices)]
        parentDict = {}
        q = queue.Queue()
        
        q.put(v1)
        
        while not q.empty():
            frontElement = q.get()
            
            if frontElement == v2:
                return parentDict
            
            visitedArray[frontElement] = True
            
            for col in range(self.nVertices):
                if self.adjMatrix[frontElement][col] == 1 and visitedArray[col] is False:
                    q.put(col)
                    parentDict[col] = frontElement
                    visitedArray[col] = True
                     
                    
        return None
                    
    def getPathBfs(self,v1,v2):
        parentDict =  self.getPathBfsHelper(v1,v2)
        if parentDict==None:
            print()
        else:
            while v2!=v1:
                for data in parentDict:
                    if data == v2:
                        print(data,end=" ")
                        v2 = parentDict[data]
            print(v2)
            
vert ,edge = list(map(int,input().split()))     
g = Graph(vert)            

edges = [[int(j)for j in input().split()] for i in range(edge)]

for data in edges:
    g.addPath(data[0],data[1])
    
v1,v2 = list(map(int,input().split()))

g.getPathBfs(v1,v2)
