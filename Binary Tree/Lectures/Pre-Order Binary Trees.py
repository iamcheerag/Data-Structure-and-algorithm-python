# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:08:57 2020

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

def PreOrderPrint(root):
    if root is None:
        return 
    
    print(root.data)
    if root.left is not None:
        PreOrderPrint(root.left)
        
    if root.right is not None:
        PreOrderPrint(root.right)
    
def postOrder(root):
    if root is None:
        return 
    
    if root.left is not None:
        postOrder(root.left)
    if root.right is not None:
        postOrder(root.right)
    
    print(root.data,end=" ")
    
root= takeInput()
PreOrderPrint(root)
postOrder(root)
    