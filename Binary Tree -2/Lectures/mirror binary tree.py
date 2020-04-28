# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:27:42 2020

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



def mirrorBinaryTree(root):
    if root is None:
        return
    
    temp = mirrorBinaryTree(root.left)
    root.left = mirrorBinaryTree(root.right)
    root.right = temp
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
    leftTree = printTree(root.left)
    rightTree = printTree(root.right)

root = takeInput()
root = mirrorBinaryTree(root)
printTree(root)