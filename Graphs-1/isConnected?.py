#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 18:44:50 2020

@author: Cheerag
"""


class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(self.nVertices)] for i in range(self.nVertices)]
        
    def addPath(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        

    
    def isConnected(self,v1,visitedArray):

        visitedArray[v1] = True

        for col in range(self.nVertices):
            if self.adjMatrix[v1][col] == 1 and visitedArray[col] is False:
                visitedArray[col] = True
                self.isConnected(col,visitedArray)
        
        return visitedArray
    
    
vert , edge = list(map(int,input().split()))

edges = [[int(i) for i in input().split()] for j in range(edge)]

g = Graph(vert)

for data in edges:
    g.addPath(data[0], data[1])

visitedArray = [False for ele in range(vert)]
        
result = g.isConnected(0,visitedArray)

if False in result:
    print('False')
else:
    print('true')

