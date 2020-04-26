# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:24:22 2020

@author: cheerag.verma
"""

class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
def takeInput():
    root = int(input())
    if root ==-1:
        return 
    btn = BinaryTree(root)
    leftTree  = takeInput()
    rightTree = takeInput()
    btn.left = leftTree
    btn.right = rightTree
    return btn

def NodeAtKDepth(root,k,count=0):
    if root == None:
        return 
    if count == k:
        print(root.data)
        return 
    NodeAtKDepth(root.left,k,count+1)
    NodeAtKDepth(root.right,k,count+1)

root = takeInput()
result = NodeAtKDepth(root,2)
print(result)

