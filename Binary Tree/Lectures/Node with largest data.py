# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:39:08 2020

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
    leftTree = takeInput()
    rightTree = takeInput()
    
    btn.left = leftTree
    btn.right = rightTree
    
    return btn



def largestNode(root):
    if root is None:
        return -1
    
    rootData = root.data
    leftLargest  = largestNode(root.left)
    rightLargest = largestNode(root.right)
    
    if rootData >= leftLargest and rootData >= rightLargest:
        return rootData
    elif leftLargest >= rootData and leftLargest >= rightLargest:
        return leftLargest
    else:
        return rightLargest
    
    
root = takeInput()
result = largestNode(root)
print(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
