#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:29:59 2020

@author: Cheerag
"""
import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(self.nVertices)] for i in range(self.nVertices)]

    def addPath(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def bfsHelper(self,v1,visitedArray):
        q = queue.Queue()
        q.put(v1)
        visitedArray[v1] = True
        
        while not q.empty():
            vertex = q.get()
            
            print(vertex,end=" ")
            for col in range(self.nVertices):
                if self.adjMatrix[vertex][col] == 1 and visitedArray[col] is False:
                    q.put(col)
                    visitedArray[col] = True
    
    def bfs(self):
        visitedArray = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visitedArray[i] is False:
                self.bfsHelper(i,visitedArray)

    def hasPath(self,v1,v2,visitedArray):
        
        visitedArray[v1] = True
        if self.adjMatrix[v1][v2] == 1: #direct edge
            return True
        
        else:
            for col in range(self.nVertices):
                if self.adjMatrix[v1][col] == 1 and visitedArray[col] is False:
                    ans = self.hasPath(col,v2,visitedArray)
                    return ans
            
            return False  


# g.addPath(0,1)
# g.addPath(0,2)
# g.addPath(2,3)
# #g.bfs()



vert , edge = list(map(int,input().split()))
g = Graph(vert)
edges = []
for i in range(edge):
    edges.append([int(j) for j in input().split()])

for data in edges:
    g.addPath(data[0], data[1])
 
visitedArray = [False for i in range(4)]
print(g.hasPath(edges[-1][0],edges[-1][1],visitedArray))
        