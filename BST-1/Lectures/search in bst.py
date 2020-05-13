# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:34:38 2020

@author: cheerag.verma
"""

class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
import queue      
def takeInputLevelWise():
    q = queue.Queue()
    rootData = int(input("Enter root:"))
    if rootData == -1:
        return None
    
    root = BinaryTree(rootData)
    q.put(root)
    while not q.empty():#while q is not empty
        currentNode=q.get()
        leftChild = int(input("Enter left child:"))
        if leftChild != -1:
            btnLeft = BinaryTree(leftChild)
            currentNode.left = btnLeft
            q.put(btnLeft)
            
        rightChild = int(input("Enter right child:"))
        if rightChild != -1:
            btnRight = BinaryTree(rightChild)
            currentNode.right = btnRight
            q.put(btnRight)
            
    return root

def searchInBST(root,k):
    if root is None:
        return 
    if root.data == k:
        return root
    if k < root.data:
        node = searchInBST(root.left,k)
    if k >= root.data:
        node = searchInBST(root.right, k)
    
    return node
        


root = takeInputLevelWise()
node = searchInBST(root,5)
if node:
    print(node.data)