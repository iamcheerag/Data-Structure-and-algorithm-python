# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:22:50 2020

@author: cheerag.verma
"""



class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    root = int(input())
    if root == -1:
        return

    btn = BinaryTree(root)
    leftTree = takeInput()
    rightTree = takeInput()
    btn.left = leftTree
    btn.right = rightTree
    
    return btn

def nodesWithoutSibling(root):
    if root is None:
        return 
    if root.left !=None and root.right == None:
        print(root.left.data)
    elif root.left == None and root.right!=None:
        print(root.right.data)
     
    
    nodesWithoutSibling(root.left)
    nodesWithoutSibling(root.right)
    
    
    
root = takeInput()
result = nodesWithoutSibling(root)
print(result)