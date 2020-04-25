# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:31:03 2020

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


def printNodeSum(root):
    if root is None:
        return 0
    data = root.data
    left = printNodeSum(root.left)
    right = printNodeSum(root.right)
    return data + left+right

root = takeInput()
sumOfNodes = printNodeSum(root)
print(sumOfNodes)