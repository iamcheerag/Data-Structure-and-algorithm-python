# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:01:30 2020

@author: cheerag.verma
"""


class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =None

import queue    
def takeInputLevelOrder():
    rootData = int(input("Enter root:"))
    if rootData == -1:
        return 
    root = BinaryTree(rootData)
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        current = q.get()
        leftChildData = int(input("Enter left Child:"))
        if leftChildData != -1:
            leftChild = BinaryTree(leftChildData)
            current.left = leftChild
            q.put(leftChild)
            
            
        rightChildData = int(input("Enter right Child:"))
        if rightChildData != -1:
            rightChild = BinaryTree(rightChildData)
            current.right = rightChild
            q.put(rightChild)


    return root

    
    
def rootToLeafPathsSumToK(root, k, lst=[]):
    if root is None:
        return
    
    if root.left == None and root.right == None:
        if k == root.data:
            print(*lst,root.data)
            return 
        
    lst.append(root.data)
    rootToLeafPathsSumToK(root.left,k-root.data,lst)
    rootToLeafPathsSumToK(root.right,k-root.data,lst)
    del lst[-1]
                
            
root = takeInputLevelOrder()
rootToLeafPathsSumToK(root,13)

       
    
    
    
    
    
    
            
    