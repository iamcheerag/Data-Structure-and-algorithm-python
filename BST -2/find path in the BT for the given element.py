# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:03:27 2020

@author: cheerag.verma
"""
"""
Given a Binary Tree , find and returns the path of the element to searched in BT"""

import queue
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
def takeInput():
    rootData = int(input("Enter root :"))
    if rootData == None:
        return 
    root = BinaryTree(rootData)
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        curr = q.get()
        leftData = int(input("Enter left child:"))
        if leftData!=-1:
            leftTree = BinaryTree(leftData)
            curr.left = leftTree
            q.put(leftTree)
            
        rightData = int(input("Enter right child:"))
        if rightData!=-1:
            rightTree = BinaryTree(rightData)
            curr.right = rightTree
            q.put(rightTree)
            
    return root

def rootToNodePath(root,element,a=[]):
    if root == None:
        return 
    
    if root.data == element:
        print(root.data)
        for i in range(len(a)-1,-1,-1):
            print(a[i])
    
    a.append(root.data)
    rootToNodePath(root.left,element,a)
    rootToNodePath(root.right,element,a)
    del(a[-1])
    
root = takeInput()
rootToNodePath(root,5)
 
    
    
    
    
            
            