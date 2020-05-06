# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:56:15 2020

@author: cheerag.verma
"""


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    if len(lst) == 0:
        return 
    
    mid = len(lst)//2
    
    root = BinaryTreeNode(lst[mid])
    root.left = constructBST(lst[:mid])
    root.right = constructBST(lst[mid+1:])
    return root

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=constructBST(lst)
preOrder(root)
