# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:49:49 2020

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

def NumberOfNode(root):
    if root is None:
        return 0
    left = NumberOfNode(root.left)
    right = NumberOfNode(root.right)
    return 1+left+right

def printBinaryTree(root):
    
    if root is None:
        return 
    print(root.data,end=":")
    if root.left is not None:
        print("L",root.left.data,end=",")
    if root.right is not None:
        print("R",root.right.data,end="")
    print()
    
    printBinaryTree(root.left)
    printBinaryTree(root.right)
    
    
root = takeInput()
printBinaryTree(root)
# totalNodes = NumberOfNode(root)
# print(totalNodes)
    