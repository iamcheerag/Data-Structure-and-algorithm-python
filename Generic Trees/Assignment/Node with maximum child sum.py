# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:48:40 2020

@author: CHEERAG
"""

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def maxSumNode(root,sum):
    if root == None:
        return 
    
    ans = root
    sum = root.data
    
    for child in root.children:
        sum = sum + child.data
    
    for child in root.children:
        tempNode,tempSum = maxSumNode(child,sum)
        
        if tempSum>sum:
            sum = tempSum
            ans = tempNode
        
    
    return ans,sum
        
    
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
temp, tempSum = maxSumNode(tree)
print(temp.data)
