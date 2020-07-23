#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:17:45 2020

@author: Cheerag
"""

import sys
class graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(self.nVertices)] for i in range(self.nVertices)]
        
    def addEdge(self,v1,v2,wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt
        
    
    def getminVertex(self,weight,visited):
        minVertex = -1
        
        for i in range(self.nVertices):
            if visited[i] is False and (minVertex == -1 or weight[minVertex]> weight[i]):
                minVertex = i
        
    
    def prims(self):
        visited = [False for i in range(self.nVertices)]
        weight  = [sys.maxsize for i in range(self.nVertices)]
        parent  = [-1 for i in range(self.nVertices)]
        weight[0] = 0
        for i in range(self.nVertices-1):
            minVertex = self.getminVertex(weight,visited) # vertex which is not visited and have min weight
            visited[minVertex] = True
            
            
            #Explore neighbours of minvertex and update the corresponding wt if required
            
            for j in range(self.nVertices):
                if self.adjMatrix[minVertex][j] > 0 and visited[j] is False:
                    if (weight[j] > self.adjMatrix[minVertex][j]):
                        weight[j] = self.adjMatrix[minVertex][j]
                        parent[j] = minVertex
            
        
        for i in range(1,self.nVertices):
            if i > parent[i]:
                print(i," ",parent[i]," ",weight[i])
    
            else:
                print(parent[i]," ",i," ",weight[i])
    
    
        
vert,edges = list(map(int,input().split()))

g = graph(vert)
for i in range(edges):
    inputArray = [int(i) for i in input().split()]
    g.addEdge(inputArray[0],inputArray[1],inputArray[2])
    
g.prims()    


        