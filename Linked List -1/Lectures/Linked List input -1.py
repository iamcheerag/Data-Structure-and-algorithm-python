# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:30:31 2020

@author: cheerag.verma
"""
""" Not a best to take input of the linkedlist since time complexity is O(n2)"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    
def inputElement():
    
    inputArray = [int(element) for element in input().split()]
    head = None
    for ele in inputArray:
        if ele == -1:
            break
        
        newNode = Node(ele)
        
        if head is None:  # This will occur only for the first element of the linkedlist
            head = newNode
        
        else:   
            current = head
            while current.next is not None:
                current = current.next
            
            current.next = newNode
        
    return head
    

def printLL(headOfLinkedList):
    current =headOfLinkedList
    
    while current is not None:
        print(str(current.data) + "-->",end= " ")
        current = current.next
    print("None")
    

headOfLinkedList = inputElement()
printLL(headOfLinkedList)

