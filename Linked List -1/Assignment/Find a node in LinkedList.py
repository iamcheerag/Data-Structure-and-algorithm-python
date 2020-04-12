# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 01:40:30 2020

@author: cheerag.verma
"""
"""
Find a node in LL

Given a linked list and an integer n you need to find and return index where n is present in the LL. Do this iteratively.
Return -1 if n is not present in the LL.
Indexing of nodes starts from 0.
    Input format :
    Line 1 : Linked list elements (separated by space and terminated by -1)
    Line 2 : Integer n 
    Output format  : Index
    
    Sample Input 1  : 3 4 5 2 6 1 9 -1
                      5
    Sample Output 1 : 2
   
    Sample Input 2  : 3 4 5 2 6 1 9 -1
                      6
    Sample Output 2 : 4
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
    

def linearSearch(head,n):
    current = head
    count=0
    while current is not None:
        if current.data == n:
            break
        else:
            current = current.next
            count+=1
    else:
        return -1
    
    return count
    
arr = [int(x) for x in input().split()]
head = createLinkedList(arr[:-1])
n = int(input())
result = linearSearch(head,n)
print(result)