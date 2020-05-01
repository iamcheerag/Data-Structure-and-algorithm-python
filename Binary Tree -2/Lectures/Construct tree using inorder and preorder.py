# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:48:34 2020

@author: cheerag.verma

"""
       
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def buildTreeFromInorderAndPreorder(preorder,inorder):
    if len(preorder) == 0 or len(inorder) == 0 :
        return 
    
    root = BinaryTree(preorder[0])
    
    if root is None:
        return 
    index = 0
    for i in range(len(inorder)):
        if inorder[i] == root.data:
            index = i
            #print("root",root.data)
            #print("index:",index)
            break
            
    leftInorder = inorder[:index]
    rightInorder = inorder[index+1:]
        
    leftPreorder = preorder[1:len(leftInorder)+1]
    rightPreorder = preorder[len(leftInorder)+1:]
    
    root.left = buildTreeFromInorderAndPreorder(leftPreorder,leftInorder)
    root.right = buildTreeFromInorderAndPreorder(rightPreorder,rightInorder)
    
    return root

import queue   
def printTree(root):
    if root is None:
        return
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        current_element = q.get()
        print(current_element.data,end=" ")
        if current_element.left is not None:
            q.put(current_element.left)
            
    
        if current_element.right is not None:
            q.put(current_element.right)
        print()
            
#inorder =  [1, 2 ,3 ,4 ,15 ,5 ,6 ,7 ,8 ,10, 9 ,12]     
#preorder = [4 ,15, 3 ,2 ,5 ,1 ,6 ,10 ,8 ,7 ,9 ,12]

preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreeFromInorderAndPreorder(preorder,inorder)
printTree(root)



            
            
            
            
            
    
    
    
        
        
        


