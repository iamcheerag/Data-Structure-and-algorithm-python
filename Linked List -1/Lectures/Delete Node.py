# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:06:27 2020

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
    current = head
    count = 0
    while current is not None:
        current = current.next
        count+=1
    return count


def deleteNode(head,index):
    current = head
    prev = None
    count = 0
    n = lenghtLinkedList(head)
    if index < 0 or index > n-1:
        return head
    
    while current is not None:
        if count == index:
            #current = current.next
            break
        
        else:
            prev = current
            current = current.next
            count+=1
            
    if prev is None:
        head = current.next   # i have moved the current in while loop
        
    else:    
        prev.next = current.next
    
    return head

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
head = deleteNode(head,5)
printLinkedList(head)