# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:07:54 2020

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

def lengthLL(head):
    if head is None:
        return 0
    else:
        return 1 + lengthLL(head.next)


def insertNodeAtIthPositionRecursively(head,index,data):
    l = lengthLL(head)
    
    if index < 0 and index > l:
        return head
    
    if head is None:
        return 0
    if index == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    
    smallhead = insertNodeAtIthPositionRecursively(head.next,index-1,data)
    head.next = smallhead
    
    return head    
    
    
def printLinkedList(head):
    current = head
    while current is not None:
        print(str(current.data)+" ->",end= " ")
        current = current.next
    print("None")


inputArr = [int(x) for x in input().split()]
head = createLinkedList(inputArr[:-1])
printLinkedList(head)
head = insertNodeAtIthPositionRecursively(head,3,10)
printLinkedList(head)
