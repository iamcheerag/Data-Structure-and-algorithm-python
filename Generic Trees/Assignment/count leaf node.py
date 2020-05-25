# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:01:28 2020

@author: CHEERAG
"""

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def __str__(self):
        return str(self.data)

def leafNodeCount(root):
    if root == None:
        return 
    
    if len(root.children) == 0:
        return 1
    
    resultCount=0
    for child in root.children:
        resultCount = resultCount + leafNodeCount(child)    
    return resultCount
    
def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(leafNodeCount(tree))
