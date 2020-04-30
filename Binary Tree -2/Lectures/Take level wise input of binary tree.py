# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 00:41:50 2020

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
    rootData = int(input("Enter the root"))
    if rootData == -1:
        return None
    
    root = BinaryTree(rootData)
    q.put(root)
    print("-----------")
    while not q.empty():#while q is not empty
        currentNode=q.get()
        leftChild = int(input("Enter the left child"))
        if leftChild != -1:
            btnLeft = BinaryTree(leftChild)
            currentNode.left = btnLeft
            q.put(btnLeft)
            
        rightChild = int(input("Enter the right child"))
        if rightChild != -1:
            btnRight = BinaryTree(rightChild)
            currentNode.right = btnRight
            q.put(btnRight)
            
            
        
    return root
        
def printBinaryTree(root):
    if root == None:
        return 
    
    print(root.data,end = " ")
    printBinaryTree(root.left)
    printBinaryTree(root.right)
    
    
    
root = takeInputLevelWise()
printBinaryTree(root)
        
        
    
    
    
    
    
    
    