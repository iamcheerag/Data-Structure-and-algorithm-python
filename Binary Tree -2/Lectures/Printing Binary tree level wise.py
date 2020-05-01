# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:09:13 2020

@author: cheerag.verma
"""


class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
import queue      

def takeInputLevelwise():
    q = queue.Queue()
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    q.put(root)
    
    while not q.empty():
        current_element = q.get()
        
        leftChild = int(input())
        if leftChild!=-1:
            leftChild = BinaryTree(leftChild)
            current_element.left = leftChild
            q.put(leftChild)
            
        rightChild = int(input())
        if rightChild!=-1:
            rightChild = BinaryTree(rightChild)
            current_element.right = rightChild
            q.put(rightChild)
        
    return root
    
    
def printBinaryTreePreOrder(root):
    if root == None:
        return 
    print(root.data,end=" ")
    printBinaryTreePreOrder(root.left)
    printBinaryTreePreOrder(root.right) 


def printBinaryTreeLevelwise(root):
    if root == None:
        return 
    
    q = queue.Queue()
    
    if root.data !=-1:
        q.put(root)
        
    while not q.empty():
        root = q.get()
        print(root.data,end=":")
        if root.left is not None:
            print("L:"+str(root.left.data),end=",")
            q.put(root.left)
        if root.left is None:
            print("L:"+str(-1),end=",")
            
        if root.right is not None:
            print("R:"+str(root.right.data))
            q.put(root.right)
            
        if root.right is None:
            print("R:"+str(-1))
            
root = takeInputLevelwise()
#printBinaryTreePreOrder(root)
printBinaryTreeLevelwise(root)
    
    
    
    
    
    
    
    
