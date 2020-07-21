#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:24:28 2020

@author: Cheerag
"""

class graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(nVertices)]for i in range(nVertices)]
        
    def addEdge(self,v1,v2):
        
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
    def removeEdge(self,v1,v2):
        if self.isEdgePresent(v1, v2) is True:
            self.adjMatrix[v1][v2] = 0
            self.adjMatrix[v2][v1] = 0
        else:
            return 
        
        
    def isEdgePresent(self,v1,v2):
        if self.adjMatrix[v1][v2] > 0 :
            return True
        else:
            return False
 
    def bfsHelper(self,visitedArray,startingVertex):
        print(startingVertex)
        visitedArray[startingVertex] = True
        
        for col in range(self.nVertices):
            if self.adjMatrix[startingVertex][col] == 1 and visitedArray[col] is False:
                self.bfsHelper(visitedArray, col)
            

    def bfs(self):
        visitedArray = [False for i in range(self.nVertices)]
        self.bfsHelper(visitedArray,0)

       
    def __str__(self):
        return str(self.adjMatrix)
    
g = graph(6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(3, 5)
g.addEdge(2, 4)
g.addEdge(1, 5)
# print(g.isEdgePresent(1,5))
# g.removeEdge(1, 5)
# print(g.isEdgePresent(1,5))
# print(g)
g.bfs()

        
        