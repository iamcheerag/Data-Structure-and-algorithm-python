# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:27:49 2020

@author: cheerag.verma
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
def createLL(arr):
    if len(arr)== 0:
        return 
    
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    
    return head

def reverseLLR(head):
    if head.next is None:
        return
    
    reverseLLR(head.next)
    
    print(head.data,end=" ")
    return 

def printLL(head):
    current = head
    while current is not None:
        print(current.data,end= " ")
        current = current.next
        
        
arr = [int(x) for x in input().split()]
head = createLL(arr[:-1])
reverseLLR(head)
head = reverseLLR(head)
printLL(head)