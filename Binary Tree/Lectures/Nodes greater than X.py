# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:51:10 2020

@author: cheerag.verma
"""


"""
Nodes Greater Than X

Given a Binary Tree and an integer x, find and return the count of nodes which are having data greater than x.
    Input format :
    Line 1 : Elements in level order form (separated by space)
    (If any node does not have left or right child, take -1 in its place)
    Line 2 : Integer x
    Output Format :
    count
    Sample Input :
    8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
    8
    Sample Output :
    3               
"""


class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None
        
def takeInput():  #preOrder
    root = int(input())
    if root == -1:
        return 
    btn = BinaryTree(root)
    
    leftTree = takeInput()
    rightTree = takeInput()
    
    btn.left = leftTree
    btn.right = rightTree
    
    
    return btn


def NodesGreaterThanX(root,x):
    count = 0
    if root is None:
        return 0
    
    if root.data > x:
        count+=1
    
    leftCount = NodesGreaterThanX(root.left,x)
    rightCount = NodesGreaterThanX(root.right,x)
    return leftCount + rightCount +count

root = takeInput()
result = NodesGreaterThanX(root,6,0)
print(result)

    
    
    
    
    
    
    
    
    
    
    
    
    