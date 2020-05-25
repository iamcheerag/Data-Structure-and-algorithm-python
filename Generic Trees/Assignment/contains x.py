# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:41:29 2020

@author: CHEERAG
"""

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def containsX(root, x):
    if root == None:
        return False #edge case not a base case
    
    if root.data == x:
        return True
    
    for child in root.children:
        result = containsX(child, x)
        if result == True:
            return True
        
    return False    
        
        
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
x=int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
if containsX(tree,x):
    print('true')
else:
    print('false')
