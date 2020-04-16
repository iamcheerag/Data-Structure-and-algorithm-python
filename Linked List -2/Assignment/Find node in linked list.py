# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:19:51 2020

@author: cheerag.verma
"""

"""
Find a node in LL (recursive)

Given a linked list and an integer n you need to find and return index where n is present in the LL. Do this recursively.
Return -1 if n is not present in the LL.
Indexing of nodes starts from 0.
    Input format :
    Line 1 : Linked list elements (separated by space and terminated by -1)
    Line 2 : Integer n 
    
    Output format :
    Index
    
    Sample Input 1 :
    3 4 5 2 6 1 9 -1
    5
    Sample Output 1 :
    2
    
    Sample Input 2 :
    3 4 5 2 6 1 9 -1
    6
    Sample Output 2 :
    4
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linearSearchRecursive(head,n,si):
        if head is None:
            return None
        if head.next is None:
            if head.data == n:
                return si
            else:
                return -1
            
        if head.data == n:
            return si
        else:
            smallOutput = linearSearchRecursive(head.next,n,si+1)
            return smallOutput

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
data=int(input())
index = linearSearchRecursive(l, data,0)
print(index)


























