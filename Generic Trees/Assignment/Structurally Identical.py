# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:37:41 2020

@author: CHEERAG
"""

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(root1, root2):
    if root1 == None or root2 == None:
        return
    
    if root1.data == root2.data:
        return True
    
    
    for child1,child2 in zip(root1.children,root2.children):
        result = isIdentical(child1,child2)
    
    
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
arr1 = list(int(x) for x in input().strip().split(' '))
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in input().strip().split(' '))
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')
