# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:41:37 2020

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

def removeLeafNode(root):
    if root is None:
        return 
    
    if root.left == None and root.right == None:  #to check leaf node
        return None
    root.left = removeLeafNode(root.left)
    root.right = removeLeafNode(root.right)
    
    return root

def printTree(root):
    if root is None:
        return 
    
    print("root:",root.data,end="-")
    if root.left is not None:
        print("L:",root.left.data,end=",")
    if root.right is not None:
        print("R:",root.right.data,end="")
    print()
    printTree(root.left)
    printTree(root.right)
    
    
    
    
root = takeInput()
root = removeLeafNode(root)
printTree(root)
        
    