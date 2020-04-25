# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:12:23 2020

@author: cheerag.verma
"""


class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def printBT(root):   # this method doesn't give me all the information. who is parent and who is child
    if root is None:
        return 
    print(root.data)
    printBT(root.left)
    printBT(root.right)
    
    
def printBTdetailed(root):
    if root is None:
        return
    print("Root",root.data,end=":")
    if root.left is not None:
        print("L",root.left.data,end=",")
    if root.right is not None:
        print("R",root.right.data,end="")
    print()
    printBTdetailed(root.left)
    printBTdetailed(root.right)
    

btn1 = BinaryTree(2)
btn2 = BinaryTree(12)
btn3 = BinaryTree(22)
btn4 = BinaryTree(23)
btn5 = BinaryTree(4)
btn6 = BinaryTree(20)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5
btn3.right = btn6

printBTdetailed(btn1)
