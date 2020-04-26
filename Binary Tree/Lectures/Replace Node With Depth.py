# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:57:39 2020

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

def replaceWithDepth(root,k=0):
    if root is None:
        return 
    root.data = k
    replaceWithDepth(root.left , k +1)
    replaceWithDepth(root.right , k +1)
    return 
    
root = takeInput()
replaceWithDepth(root)