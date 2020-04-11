# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 22:27:03 2020

@author: cheerag.verma
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteRec(head, i):
    if head is None:
        return head
    
    if i ==0:
        current = head
        head = current.next
        return head
    smallHead = deleteRec(head.next,i-1)
    head.next = smallHead
    return head

    

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = deleteRec(l, i)
printll(l)
