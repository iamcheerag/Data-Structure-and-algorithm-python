# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 00:23:01 2020

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

def reverseLinkedListRecursionOptimized(head):
    if head.next is None:
        return head,head
    
    smallHead,smallTail = reverseLinkedListRecursionOptimized(head.next) # induction step 

    smallTail.next = head
    head.next = None
    
    return smallHead,head
    
    
def printLinkedList(head):
    
    current = head
    while current is not None:
        print(current.data,end=" ")
        current = current.next
        
    
    
arr = list(map(int,input().split()))
head = createLL(arr[:-1])
head ,tail = reverseLinkedListRecursionOptimized(head)
printLinkedList(head)

