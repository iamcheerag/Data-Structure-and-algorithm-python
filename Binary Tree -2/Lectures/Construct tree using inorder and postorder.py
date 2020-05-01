# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:24:09 2020

@author: cheerag.verma
"""


class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def constructTreeUsingInorderAndPostorder(inorder,postorder):
    if len(postorder) == 0 or len(inorder) == 0 :
        return None
    
    root = BinaryTree(postorder[-1])
    index = 0
    for i in range(len(inorder)):
        if inorder[i] == root.data:
            index = i
            break
        
    leftInorder = inorder[:index]
    rightInorder = inorder[index+1:]
    
    leftPostorder = postorder[:len(leftInorder)]
    rightPostorder = postorder[len(leftInorder):-1]
    
    root.left = constructTreeUsingInorderAndPostorder(leftInorder,leftPostorder)
    root.right = constructTreeUsingInorderAndPostorder(rightInorder,rightPostorder)
    
    return root

import queue
def printTree(root):
    if root is None:
        return 
    q = queue.Queue()
    
    q.put(root,end=":")
    while not q.empty():
        current = q.get()
        print(current.data,end=" ")
        
        if current.left is not None:
            q.put(current.left)
        
        if current.right is not None:
            q.put(current.right)
        
        print()
    
 
inorder   = [4 ,15 ,3 ,2 ,5 ,1 ,6 ,10 ,8 ,7 ,9 ,12]
postorder = [15 ,4 ,3 ,5 ,2 ,10 ,8 ,12, 9 ,7 ,6 ,1]
root = constructTreeUsingInorderAndPostorder(inorder,postorder)
printTree(root)




