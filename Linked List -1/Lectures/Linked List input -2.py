# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:26:46 2020

@author: cheerag.verma
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:30:31 2020

@author: cheerag.verma
"""
""" time complexity - O(n2)"""
        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
        
def inputLinkedList():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for ele in inputList:
        if ele == -1:
            break
    
        newNode = Node(ele)
        if head is None:
            head = newNode
            tail = newNode
        
        else:
            tail.next = newNode 
            tail = newNode
            
    return head
            
        
def printLinkedList(head):
    current = head
    
    while current is not None:
        print(str(current.data)+"->",end = " ")
        current = current.next
    print("None")
    
if __name__ == "__main__":
    head = inputLinkedList()
    printLinkedList(head)