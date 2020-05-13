# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:50:33 2020

@author: cheerag.verma
"""

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self, root):
        if root == None:
            return
        
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)
    
    def isSearchHelper(self,root,data):
        if root == None:
            return False
        
        if root.data == data:
            return True
        
        if root.data > data:#left tree
            return self.isSearchHelper(root.left,data)
        
        else:
            return self.isSearchHelper(root.right,data)
    
    def search(self, data):
        return self.isSearchHelper(self.root, data)
        
    def insertHelper(self,root,data):
        if root == None:
            root = BinaryTreeNode(data)
            return root
            
        if root.data > data: #left subtree
            root.left  = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root

    
    def insert(self, data):
        self.numNodes+=1
        self.root = self.insertHelper(self.root,data)
        
    def min(self,root):
        if root == None:
            return 100000
            
        if root.left == None:
            return root.data
        
        return self.min(root.left)
    
    
    def deleteHelper(self,root,data):
        if root == None:
            return False,None
        
        if root.data < data:
            deleted,rightRoot = self.deleteHelper(root.right,data)
            root.right = rightRoot
            return deleted,root
            
        if root.data > data:
            deleted , leftRoot = self.deleteHelper(root.left,data)
            root.left = leftRoot
            return deleted,root
            
        # root is leaf
        if root.left == None and root.right == None:
                return True,None
        
        #root has 1 child
        if root.left== None:
            return True,root.right
         
        if root.right == None:
            return True,root.left  #left child to be new root
        
        #root has 2 children
        replacement = self.min(root.right) # getting min from right subtree
        root.data = replacement  #coping the min from right subtree to the root
        deleted, rightRoot = self.deleteHelper(root.right,replacement)
        root.right = rightRoot
        return True,root
    
         
        
    def delete(self, data):
        deleted,newRoot =  self.deleteHelper(self.root,data)
        if deleted:
            self.numNodes-=1
        self.root = newRoot
        return deleted
    
    
    def count(self):
        return self.numNodes


b = BST()
li = [int(ele) for ele in input().split()]
i = 0
while(i < (len(li) )):
    choice = li[i]
    if choice == 1:
        data = li[i+1]
        b.insert(data)
        i+=2
    elif choice == 2:
        data = li[i+1]
        b.delete(data)
        i+=2
    elif choice == 3:
        data = li[i+1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
        i+=2
    else:
        b.printTree()
        i+=1
        
