# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:11:52 2020

@author: cheerag.verma
"""


"""
Level order traversal

Given a binary tree, print the level order traversal. Make sure each level start in new line.
Input format :

Elements in level order form (separated by space). If any node does not have left or right child, take -1 in its place.

Output Format :

Elements are printed level wise, each level in new line (separated by space).

Sample Input :
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
Sample Output :
5 
6 10 
2 3 
9
"""


class BinaryTree:
    def __init__(self,data):
        self.data  = data
        self.left  = None
        self.right = None

import queue
def takeInputLevelOrder():
    q = queue.Queue()
    rootData = int(input("Enter root"))
    if rootData == -1:
        return 
    
    root = BinaryTree(rootData)
    q.put(root)
    
    while not q.empty():
        current = q.get()
        
        leftCurrent = int(input("Enter left child"))
        if leftCurrent!=-1:
            leftChild = BinaryTree(leftCurrent)
            current.left = leftChild
            q.put(leftChild)
         
        rightCurrent = int(input("Enter right child"))               
        if rightCurrent!=-1:
            rightChild = BinaryTree(rightCurrent)
            current.right = rightChild
            q.put(rightChild)
            
    return root

def printLevelATNewLine(root):
    if root is None:
        return
    
    q = queue.Queue() 
    q.put(root)

    q1= queue.Queue()
    while not q.empty():
        while not q.empty():
            root = q.get()
            print(root.data,end=" ")
            if root.left is not None:
                q1.put(root.left)
            if root.right is not None:
                q1.put(root.right)
        print()
        q,q1=q1,q
        
        
root = takeInputLevelOrder()
printLevelATNewLine(root)
