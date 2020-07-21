## Read input as specified in the question.
## Print output as specified in the question.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:29:59 2020

@author: Cheerag
"""
"""
Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), check if there exists any path between them or not. Print true or false.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
    Input Format :
    Line 1: Two Integers V and E (separated by space)
    Next E lines : Two integers a and b, denoting that there exists an edge between vertex a and vertex b (separated by space)
    Line (E+2) : Two integers v1 and v2 (separated by space)
    Output Format :
    true or false
    Constraints :
    2 <= V <= 1000
    1 <= E <= 1000
    0 <= v1, v2 <= V-1
    Sample Input 1 :
    4 4
    0 1
    0 3
    1 2
    2 3
    1 3
"""
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(self.nVertices)] for i in range(self.nVertices)]

    def addPath(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def hasPath(self,v1,v2,visitedArray):  #dfs implementation
        
        visitedArray[v1] = True
        if self.adjMatrix[v1][v2] == 1 or self.adjMatrix[v2][v1] ==1 : #direct edge
            return True
        
        else:
            for col in range(self.nVertices):
                if self.adjMatrix[v1][col] == 1 and visitedArray[col] is False:
                    visitedArray[col] = True
                    ans = self.hasPath(col,v2,visitedArray)
                    if ans is True:
                        return ans
            
        return False  


vert , edge = list(map(int,input().split()))
g = Graph(vert)
edges = []
for i in range(edge):
    edges.append([int(j) for j in input().split()])

for data in edges:
    g.addPath(data[0], data[1])

str1=input().split()
v1,v2=int(str1[0]),int(str1[1])
visitedArray = [False for i in range(vert)]
result = (g.hasPath(v1,v2,visitedArray))

if result:
    print("true")
else:
    print("false")
        