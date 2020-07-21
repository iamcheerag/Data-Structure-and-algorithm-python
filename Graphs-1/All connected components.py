#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 20:41:22 2020

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
        
    def allConnectedComponentHelper(self,v1,visitedArray):
        
        q = queue.Queue()
        q.put(v1)
        output = []
        visitedArray[v1] = True
        while not q.empty():
            element = q.get()
            output.append(element)
            
            for col in range(self.nVertices):
                if self.adjMatrix[element][col] == 1 and visitedArray[col] is False:
                    print(element,col)
                    q.put(col)
                    visitedArray[col] = True
        
        return output        
         
    def allConnectedComponent(self):
        visitedArray = [False for i in range(self.nVertices)]
        ans = []
        for i in range(self.nVertices):
            if visitedArray[i] == False:
                result = self.allConnectedComponentHelper(i,visitedArray)
                ans.append(result)
        return ans
                
# g = Graph(3)
# g.addPath(0,1)    

g = Graph(9)
g.addPath(0, 1)
g.addPath(0 ,2)
g.addPath(0, 3)
g.addPath(2, 7)
g.addPath(2, 8)
g.addPath(3, 4)
g.addPath(3, 6)
g.addPath(4, 5)
# g.addPath(8, 7)
#g.addPath(2,8)

ans = (
       ag.allConnectedComponent())

ans = [8,92,1,3,14,5]
ans.sort()
for data in ans:
    print(data)
    
            