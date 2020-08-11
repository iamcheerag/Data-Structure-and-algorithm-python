#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 19:34:08 2020

@author: Cheerag
"""


class Node:
    def __init__(self,data):
        '''
        Linked list node creation with data in input and next as None
        '''
        self.data = data
        self.next = None
        
        
def createLinkedList(arr):
    '''
    This function generates the linked list
    '''
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next

    return head

def lenghtOfLinkedList(head):
    if head is None:
        return 0
    
    return 1+lenghtOfLinkedList(head.next)


def insertNode(head,index,data):
    '''
    This function inserts the nodes at any position in the linkedList
    '''
    l = lenghtOfLinkedList(head)
    
    if index <0 or index > l:
        return head
    
    count = 0
    current = head
    prev = None
    while current is not None:   # This loop helps in finding the correct insert position
        if count == index:
            break       
        else:
            prev = current
            current = current.next
            count +=1
            
    newNode = Node(data)
    if prev is None:            # Insertion at beginning
        newNode.next = head
        head = newNode
    else:
        prev.next = newNode     # Insertion at specific position
        newNode.next = current
     
    return head
    

def deleteNode(head,index):
    '''
    This function deletes the node at any position in the linkedList
    '''
    l= lenghtOfLinkedList(head)
    
    if index <0 or index > l:
        return head
    
    current = head
    count = 0
    prev = None
    while current is not None:   # This loop helps in finding the correct index before deletion
        if count == index: 
            break
        else:
            count+=1
            prev    = current
            current = current.next
    
    if prev is None:
        head = current.next       # deletion from beginning
    else:
        prev.next = current.next  #deletion from any index
    return head
    


def printLinkedList(head):
    '''
    This function prints the linkedList
    '''
    curr = head
    while curr is not None:
        print(curr.data,end="--")
        curr = curr.next
    print("None")
    
    
ll   = list(map(int,input().split()))
head = createLinkedList(ll[:-1])
#printLinkedList(head)

flag = True
while flag:
    print('Select-1:For insertion')
    print('Select-2:For Deletion')
    print('Select-3:For Printing Linked List')
    i = int(input())
    if i<0 or i>4:
        flag = False
    if i ==1:    
        #Linked list insertion
        head = insertNode(head,int(input('Enter index')),int(input('Enter data')))
        printLinkedList(head)
    
    if i == 2:
        #Linked list deletion
        head = deleteNode(head,int(input('Enter Index to be deleted')))
        printLinkedList(head)
        
    if i == 3:
        printLinkedList(head)