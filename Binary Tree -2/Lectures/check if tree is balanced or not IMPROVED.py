# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:29:48 2020

@author: cheerag.verma

Time Complexity = O(n)

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


def isBalancedOptimized(root):
    if root is None:
        return 0,True
    
    heightLeft,leftTreeBalanced = isBalancedOptimized(root.left)
    heightRight,rightTreeBalanced = isBalancedOptimized(root.right)
    
    h = 1+max(heightLeft,heightRight)
    
    if heightLeft-heightRight>1 or heightRight-heightLeft>1:
        return h,False
    
    
    if leftTreeBalanced and rightTreeBalanced:
        return h,True
    else:
        return h,False
    
    
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
print(isBalancedOptimized(root))
#printTree(root)
    
    