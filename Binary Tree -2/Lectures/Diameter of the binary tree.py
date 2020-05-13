# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:55:25 2020

@author: cheerag.verma
"""


"""
Diameter Of Binary Tree
    Given a Binary Tree, find and return the diameter of input binary tree.
    Diameter is - largest count of nodes between any two leaf nodes in the binary tree (both the leaf nodes are inclusive).
    Input format :
        Elements in level order form (separated by space)
        (If any node does not have left or right child, take -1 in its place)
    Output Format :
        diameter
    Sample Input :
        8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
    Sample Output :
        7
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
    leftTree = takeInput()
    rightTree = takeInput()
    btn.left = leftTree
    btn.right = rightTree
    return btn

def heightOfBinaryTree(root):
    if root == None:
        return 0
    
    leftHeight = heightOfBinaryTree(root.left)
    rightHeight = heightOfBinaryTree(root.right)
    return 1 + max(leftHeight,rightHeight)
    
    
def diameterOfBinaryTree(root):
    if root is None:
        return 0
    lh = heightOfBinaryTree(root.left)
    rh = heightOfBinaryTree(root.right)
    
    option1 = lh + rh
    option2 = diameterOfBinaryTree(root.left)
    #print(option2)
    option3 = diameterOfBinaryTree(root.right)
    print(option3,option2)
    return max(1+option1,option2,option3)


def diameterOfBinaryTreeOptimized(root):
    if root == None:
        return 0,0
    
    leftTreeDia,Lheight = diameterOfBinaryTreeOptimized(root.left)
    rightTreeDia,Rheight = diameterOfBinaryTreeOptimized(root.right)
    
    h = 1 + max(Lheight,Rheight)
    

    return max(leftTreeDia,rightTreeDia),h


root = takeInput()
print(diameterOfBinaryTree(root))
#print(diameter,height)
#h,d = diameterOfBinaryTreeOptimized(root)
#print(d)
