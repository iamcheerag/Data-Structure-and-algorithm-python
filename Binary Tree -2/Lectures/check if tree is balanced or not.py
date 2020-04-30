# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:29:27 2020

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
    
def heightOfBT(root):
    if root is None:
        return 0
    leftTreeHeight = heightOfBT(root.left)
    rightTreeHeight = heightOfBT(root.right)
    return 1+leftTreeHeight+ rightTreeHeight

def isBalanced(root):
    if root is None:
        return 0
    
    leftTreeHeight = heightOfBT(root.left)
    rightTreeHeight = heightOfBT(root.right)
    
    if leftTreeHeight-rightTreeHeight>1 or rightTreeHeight-leftTreeHeight>1:
        return False
    
    isBalanced(root.left)
    isBalanced(root.right)
    return True
    

        
def printTree(root):
    if root is None:
        return 
    
    print("root:",root.data,end="-")
    if root.left is not None:
        print("L:",root.left.data,end=",")
    if root.right is not None:
        print("R:",root.right.data,end="")
    print()
    leftTree = printTree(root.left)
    rightTree = printTree(root.right)
    if leftTree and rightTree:
        return True
    else:
        return False


root = takeInput()
result = isBalanced(root)
print(result)

#printTree(root)



