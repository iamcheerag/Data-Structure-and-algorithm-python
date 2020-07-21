#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:07:13 2020

@author: Cheerag
"""


class Edge:
    def __init__(self,v1,v2,wt):
        self.v1 = v1
        self.v2 = v2
        self.wt = wt
        
        
        
def getParent(vertex,parentArray):
    if vertex == parentArray[vertex]:   # if my index and parent are same 
        return vertex
    
    return getParent(parentArray[vertex], parentArray) #Here we are looking for actual parent. parent of parent


        
def kruskal(nVertices,edgesArray):
    parentArray = [i for i in range(vert)]
    edgesArray = sorted(edgesArray,key = lambda x : x.wt) #sorting the array on the bases of weight
    count = 0 # to insert into n-1 edges 
    output = [] #array which contains MST
    
    i = 0 
    while count < nVertices-1:
        currentEdge = edgesArray[i]  #contain v1,v2,wt
        
        sourceParent = getParent(currentEdge.v1,parentArray)
        destinationParent = getParent(currentEdge.v2,parentArray)
        
        if sourceParent !=destinationParent:
            output.append(currentEdge)
            count+=1
            parentArray[sourceParent] = destinationParent  # groupinto 1 cluster
        i+=1
    
    return output
              
        
        
vert,edge= list(map(int,input().split()))

edgesArray = []
for i in range(edge):
    inputArray = [int(i) for i in input().split()]
    v1 = inputArray[0]
    v2 = inputArray[1]
    wt = inputArray[2]
    edges = Edge(v1,v2,wt)
    edgesArray.append(edges)
    
result = kruskal(vert,edgesArray)

for edge in result:
    if edge.v1 < edge.v2:
        print(str(v1)," ",str(v2)," ",str(wt))
    else:
        print(str(v2)," ",str(v1)," ",str(wt))


