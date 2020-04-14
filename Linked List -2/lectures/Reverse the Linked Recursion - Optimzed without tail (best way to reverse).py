# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:24:56 2020

@author: cheerag.verma
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
def createLL(arr):
    if len(arr)== 0:
        return None
    
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    
    return head

def reverseLinkedListRecursion(head):
    if head is None or head.next is None:
        return head
    
    smallHead = reverseLinkedListRecursion(head.next) # induction step    
    tail = head.next # head.next contain 2nd element's address and we still have the reference of it so we can use it
    tail.next = head
    head.next = None
    return smallHead
    
def  reverseLL(head):
    current = head
    prev = None
    while current is not None:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
    head = prev
    return head
    
def printLinkedList(head):
    
    current = head
    while current is not None:
        print(current.data,end=" ")
        current = current.next
        
    
    
#arr = list(map(int,input().split()))
arr = [int(x)for x in input().split()]
head = createLL(arr)
head = reverseLL(head)
printLinkedList(head)

