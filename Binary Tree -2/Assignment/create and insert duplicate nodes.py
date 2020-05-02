# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:07:20 2020

@author: cheerag.verma
"""
"""
Create & Insert Duplicate Node

Given a Binary Tree with N number of nodes, for each node create a new duplicate node, and insert that duplicate as left child of the original node.
Note : Root will remain same. So you just need to insert nodes in the given Binary Tree and no need to print or return anything.
    Input format :
    Elements in level order form (separated by space)
    (If any node does not have left or right child, take -1 in its place)
    
    Output Format :
    Level order traversal of updated tree. (Every level in new line)
    Constraints :
    1 <= N <= 1000
    
    Sample Input :
    8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
    
    Sample Output :
    8 
    8 10 
    5 10 
    5 6 
    2 6 7 
    2 7
"""


class BinaryTree:
    def __init__(self,data):
        self.data  = data
        self.left  = None
        self.right = None

import queue

def takeInputLevelOrder():
    q = queue.Queue()
    rootData = int(input("Enter root:"))
    if rootData == -1:
        return 
    
    root = BinaryTree(rootData)
    q.put(root)
    
    while not q.empty():
        current = q.get()
        
        leftCurrent = int(input("Enter left child:"))
        if leftCurrent!=-1:
            leftChild = BinaryTree(leftCurrent)
            current.left = leftChild
            q.put(leftChild)
         
        rightCurrent = int(input("Enter right child:"))               
        if rightCurrent!=-1:
            rightChild = BinaryTree(rightCurrent)
            current.right = rightChild
            q.put(rightChild)
            
    return root

def createAndInsertDuplicateNode(root):
    if root == None:
        return 
    
    createAndInsertDuplicateNode(root.left)
    createAndInsertDuplicateNode(root.right)
    
    temp = root.left
    root.left = BinaryTree(root.data)
    root.left.left = temp
    
    return root
    
    
def printTreeLevelOrder(root):
    if root is None:
        return
    
    q1 = queue.Queue()
    q2 = queue.Queue()
    q1.put(root)
    
    while not q1.empty():
        while not q1.empty():
            current = q1.get()
            print(current.data,end=" ")
            if current.left is not None:
                q2.put(current.left)
                
            if current.right is not None:
                q2.put(current.right)
        print()
        q1,q2=q2,q1
    
    
    
            
root = takeInputLevelOrder()
root = createAndInsertDuplicateNode(root)
printTreeLevelOrder(root)
    
    


    