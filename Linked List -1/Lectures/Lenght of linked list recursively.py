# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:15:07 2020

@author: cheerag.verma
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
def createLinkedList(arr):
    head = Node(arr[0])
    tail = head
    
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    
    return head

def lenghtLinkedList(head):

    if head is None:
        return 0
    else:
        return 1 + lenghtLinkedList(head.next)
    

def printLinkedList(head):
    current = head
    while current is not None:
        print(str(current.data)+" ->",end= " ")
        current = current.next
    print("None")
    
    
inputArr = [int(i) for i in input().split()]
head = createLinkedList(inputArr[:-1])
printLinkedList(head)
lenghtLinkedList(head)
printLinkedList(head)