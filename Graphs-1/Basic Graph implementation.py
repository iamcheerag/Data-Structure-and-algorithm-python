#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:04:23 2020

@author: Cheerag
"""


class graph:
    def __init__(self,nvertices):
        self.nvertices = nvertices
        self.adjacencyMatrix = [[0 for j in range(nvertices)]for i in range(nvertices)]
        
        
    def addEdge(self,v1,v2):
        self.adjacencyMatrix[v1][v2] = 1
        self.adjacencyMatrix[v2][v1] = 1
        
        
    def removeEdge(self,v1,v2):
        if self.isEdgePresent(v1, v2):
            self.adjacencyMatrix[v1][v2] = 0
            self.adjacencyMatrix[v2][v1] = 0
        
    def isEdgePresent(self,v1,v2):
        return True if self.adjacencyMatrix[v1][v2] >0 else False
        
    def __str__(self):
        return str(self.adjacencyMatrix)
    
nvertices = 4    
g = graph(nvertices)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,3)
#g.removeEdge(0, 2)
print(g)
