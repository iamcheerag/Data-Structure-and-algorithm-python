# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:15:34 2020

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

def countLeafNode(root):
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return 1
    leftTreeLeaf = countLeafNode(root.left)
    rightTreeLeaf = countLeafNode(root.right)
    return leftTreeLeaf+ rightTreeLeaf    
    
root = takeInput()
print(countLeafNode(root))
    