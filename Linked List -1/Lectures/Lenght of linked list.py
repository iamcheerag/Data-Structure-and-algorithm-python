# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:17:35 2020

@author: cheerag.verma
"""

"""
Length of LL
Given a linked list, find and return the length of input LL. Do it iteratively.
    Input format  : Linked list elements (separated by space and terminated by -1)
    Output format : Length of LL
    Sample Input  : 3 4 5 2 6 1 9 -1
    Sample Output : 7
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
def insertElement(arr):
    if len(arr) ==0 :
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
        
    return head

def lengthofLL(head):
    current = head
    count = 0
    while current is not None:
        current=current.next
        count+=1

    return count

arr =[int(x) for x in input().split()]
head = insertElement(arr[:-1])
print(lengthofLL(head))
    

