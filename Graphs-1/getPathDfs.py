#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 09:35:08 2020

@author: Cheerag
"""

class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(self.nVertices)]for i in range(self.nVertices)]

    def addPath(self,v1,v2):
        self.adjMatrix[v1][v2] =1
        self.adjMatrix[v2][v1] =1
        
    
# =============================================================================
#     def getPathDfs(self,v1,v2,visitedArray):
#         
#         #direct path
#         visitedArray[v1] = True
#         if self.adjMatrix[v1][v2] == 1 or self.adjMatrix[v2][v1]==1:
#             output = []
#             output.append(v2)
#             output.append(v1)
#             return output
#         
#         else:
#             result = []
#             for col in range(self.nVertices):
#                 if self.adjMatrix[v1][col]==1 and visitedArray[col] is False:
#                     smallAns = self.getPathDfs(col,v2,visitedArray)
#                     for data in smallAns:
#                         result.append(data)
#                     
#                     result.append(v1)
#                     
#                     return result 
#             
#             return result
# =============================================================================
                    
    def getPathDfs(self,v1,v2,visitedArray):
        
        #direct path
        
        if v1==v2:
            #output = []
            #output.append(v2)
            #output.append(v1)
            return [v2]
        visitedArray[v1] = True
        
        #else:
            #result = []
        for col in range(self.nVertices):
            if self.adjMatrix[v1][col]==1 and visitedArray[col] is False:
                smallAns = self.getPathDfs(col,v2,visitedArray)
                #for data in smallAns:
                    #result.append(data)
                if smallAns:
                
                    smallAns.append(v1)
                    return smallAns
                
                    #return result 
            
        return None
                    



# g = Graph(5)
# g.addPath(0,1)
# g.addPath(0,2)
# g.addPath(1,3)
# g.addPath(1,4)
# visitedArray = [False for i in range(5)]
# print(g.getPathDfs(2,3,visitedArray))



        
vert ,edge = list(map(int,input().split()))     
g = Graph(vert)            

edges = [[int(j)for j in input().split()] for i in range(edge)]

for data in edges:
    g.addPath(data[0],data[1])
    
v1,v2 = list(map(int,input().split()))


visitedArray = [False for i in range(vert)]
result = g.getPathDfs(v1,v2,visitedArray)

print(*result)
