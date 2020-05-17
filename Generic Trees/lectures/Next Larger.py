# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:57:10 2020

@author: CHEERAG
"""

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(root, n):
    if root == None:
        return None
    
    
    if root.data > n:
        ans = root     
    else:
        ans = None
        
    
    for child in root.children:
        tempNode = nextLargest(child,n)
        if ans == None and tempNode!=None:
            ans = tempNode
        elif ans!= None and tempNode!=None:
            if tempNode.data < ans.data:
                ans = tempNode
            
    return ans


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
n = int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(nextLargest(tree, n).data)
