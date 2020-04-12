# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 01:55:29 2020

@author: cheerag.verma
"""
"""
AppendLastNToFirst

Given a linked list and an integer n, append the last n elements of the LL to front.
Indexing starts from 0. You don't need to print the elements, just update the elements and return the head of updated LL.
Assume given n will be smaller than length of LL.
Input format :

Line 1 : Linked list elements (separated by space and terminated by -1)`

Sample Input 1 :
1 2 3 4 5 -1
3
Sample Output 1 :
3 4 5 1 2
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


def lengthOfLL(head):
    current = head
    count = 0
    while current is not None:
        current=current.next
        count+=1

    return count

def append_LinkedList(head,n) :
    l = lengthOfLL(head)
    if n < 0 or n > l:
        return head
    
    if head is None:
        return head
        
    current = head
    tail = head
    count = 0
    while current is not None:
        if count == l-n:
            break
        else:
            prev = current
            current = current.next
            count+=1
        
    while tail.next is not None:
        tail = tail.next
      
    prev.next = None
    tail.next = head
    head = current
    
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()
    
arr = [int(x) for x in input().split()]
head = createLinkedList(arr[:-1])
n = int(input())
head = append_LinkedList(head,n)
printll(head)
