# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:49:56 2020

@author: cheerag.verma
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
def createLinkedList(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
        
    return head
    
def printLinkedList(head):
    current = head
    while current is not None:
        print(str(current.data),"->",end= " ")
        current = current.next
    print("None") # to print at the end


arr = list(map(int,input().split()))
head = createLinkedList(arr[:-1])  # excluded last element of the linkedlist which is -1
printLinkedList(head)
