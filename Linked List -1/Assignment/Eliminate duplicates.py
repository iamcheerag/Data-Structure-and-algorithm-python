# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:43:01 2020

@author: cheerag.verma
"""
"""
Eliminate duplicates from LL

Given a sorted linked list (elements are sorted in ascending order). Eliminate duplicates from the given LL, such that output LL contains only unique elements.
You don't need to print the elements, just remove duplicates and return the head of updated LL.
Input format : Linked list elements (separated by space and terminated by -1)

Sample Input 1 :
1 2 3 3 3 4 4 5 5 5 7 -1
Sample Output 1 :
1 2 3 4 5 7

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lenghtOfLL(head):
    current = head
    count = 0
    while current is not None:
        current = current.next
        count+=1
    return count

def eliminate_duplicate(head):
    if head is None:
        return None
    l = lenghtOfLL(head)
    if l == 1:
        return head
    
    current = head.next
    prev = head
    
    while current is not None:
        if prev.data == current.data:
            current = current.next
        else:
            prev.next = current
            prev = current
            current = current.next
            prev.next = None
            
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
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = eliminate_duplicate(l)
printll(l)
