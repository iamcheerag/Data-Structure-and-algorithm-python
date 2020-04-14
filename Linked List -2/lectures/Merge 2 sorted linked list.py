# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:01:05 2020

@author: cheerag.verma
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def createLL(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next

    return head  

def merge(head1,head2):
    if head1 and head2 is None:
        return None
    if head1.data >= head2.data:  #h2 smaller
        finalHead = head2
        finalTail = head2
        head2 = head2.next
    else:                       #h1 smaller
        finalHead = head1
        finalTail = head1
        head1 = head1.next
    
    while head1 is not None and head2 is not None:
        if head1.data >= head2.data:  #h2 is smaller
            finalTail.next = head2
            finalTail = finalTail.next
            head2 = head2.next
            
        else:                           #h1 is smaller
            finalTail.next = head1
            finalTail = finalTail.next
            head1 = head1.next
            
    
    
    while head1 is not None:
        finalTail.next = head1
        finalTail = finalTail.next
        head1 = head1.next
        
        
    while head2 is not None:
        finalTail.next = head2
        finalTail = finalTail.next
        head2 = head2.next
        
    
    return finalHead


def printLL(head):
    current = head
    while current is not None:
        print(current.data,end = " ")
        current = current.next

arr1 = list(map(int,input().split()))
head1 = createLL(arr1[:-1])

arr2 = list(map(int,input().split()))
head2= createLL(arr2[:-1])

head = merge(head1,head2)

printLL(head)