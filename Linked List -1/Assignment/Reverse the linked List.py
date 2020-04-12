# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:43:49 2020

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
    for data in arr:
        tail.next = Node(data)
        tail = tail.next
    
    return head

def lengthOfLinkedList(head):
    current = head
    count = 0
    while current is not None:
        current = current.next
        count +=1
    return count
    
def printLinkedListReverse(head):
    l = lengthOfLinkedList(head)
    if l == 1:
        return head
    prev = None
    current = head.next
    while current is not None:
        head.next = prev
        prev = head
        head = current 
        current = current.next
        print(head.data," ",head.next)
        
    return head

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data,end = " ")
        current = current.next

arr = list(map(int,input().split()))
head = createLinkedList(arr[:-1])
head = printLinkedListReverse(head)
printLinkedList(head)