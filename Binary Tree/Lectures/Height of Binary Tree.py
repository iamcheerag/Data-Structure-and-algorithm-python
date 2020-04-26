# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:46:52 2020

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

def heightOfBT(root):
    if root is None:  #base case , considering height of 1 node is always 1 and so on
        return 0
    
    leftTreeHeight  = heightOfBT(root.left)
    rightTreeHeight = heightOfBT(root.right)
    return max(leftTreeHeight,rightTreeHeight) + 1 # additional 1 for root node
    

root = takeInput()
result = heightOfBT(root)
print(result)