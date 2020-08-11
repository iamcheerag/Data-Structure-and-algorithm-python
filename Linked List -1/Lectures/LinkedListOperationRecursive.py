#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:55:30 2020

@author: Cheerag
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
    
def insertNode(head,index,data):
    
    if index < 0 :
        return head
    
    if index == 0:
        newNode = Node(data)
        newNode.next = head
        head = newNode
        return head
    
    smallans = insertNode(head.next, index-1, data)
    head.next = smallans
    return head


def deleteNode(head,index):
    
    if index<0:
        return head
    
    if index == 0:
        return head.next
    
    smallAns = deleteNode(head.next,index-1)
    head.next = smallAns
    return head
    

def printLinkedList(head):
    curr = head
    while curr:
        print(curr.data,end="-->")
        curr = curr.next
    print('None')
    
    
ll = list(map(int,input().split()))
head = createLinkedList(ll[:-1])
# head = insertNode(head,int(input('Enter index:')),int(input('Enter data:')))

# head = deleteNode(head,int(input('Enter index:')))
# printLinkedList(head)

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