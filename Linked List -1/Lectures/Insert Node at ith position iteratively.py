# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:59:24 2020

@author: cheerag.verma
"""

class Node:
    def __init__(self,data):
        self.data= data
        self.next = None


def createLinkedList(arr):
    head = Node(arr[0])
    tail = head
    for ele in arr[1:]:
        tail.next = Node(ele)
        tail = tail.next

    return head

def lengthLinkedList(head):
    current = head
    count= 0 
    while current is not None:
        current = current.next
        count +=1
    
    print(count)


    
def insertAtSpecificIndex(head,index,data):
    l = lengthLinkedList(head)
    
    if index < 0 or index>len(l):
        return head
    
    current= head
    count = 0
    prev = None
    while current is not None:
        if count == index:
            break
        else:
            prev = current
            current = current.next
            count+=1
    
    newNode = Node(data)
    if prev is None:
        newNode.next = current
        head = newNode
    else:
        prev.next = newNode
        newNode.next = current
        
    return head


def printLinkedList(head):
    current = head
    while current is not None:
        print(str(current.data)+" ->",end = " ")
        current = current.next
    print("None")
    
inputArray = [int(x) for x in input().split()]
head = createLinkedList(inputArray[:-1])
printLinkedList(head)
head = insertAtSpecificIndex(head,6,99)
printLinkedList(head)


