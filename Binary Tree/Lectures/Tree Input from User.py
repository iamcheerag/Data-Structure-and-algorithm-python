# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:58:39 2020

@author: cheerag.verma
"""


class BinaryTree:
    def __init__(self,data):
        self.data  = data
        self.left  = None
        self.right = None
        
        
def takeInput():       #taking input vertically but on codezen take input horizontal.
    root = int(input())
    if root == -1:
        return None
    btn = BinaryTree(root)
    leftTree  = takeInput()
    rightTree = takeInput()
    btn.left = leftTree
    btn.right= rightTree
    
    return btn

def printBT(root):
    if root is None:
        return
    print(root.data,end=":")
    if root.left is not None:
        print("L",root.left.data,end=",")
    if root.right is not None:
        print("R",root.right.data,end="")
    print()
    printBT(root.left)
    printBT(root.right)
    
    
    
root = takeInput()
printBT(root)
    
        
    
    
    
    
    
    
    