# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:47:34 2020

@author: cheerag.verma
"""

"""
Print ith node

Given a linked list and a position i, print the node at ith position.
If position i is greater than length of LL, then don't print anything.
Indexing starts from 0.
    
    Input format :Line 1 : Linked list elements (separated by space and terminated by -1)
    Line 2 : Integer i (position)
    Output format   :Element at ith position
    Sample Input 1  :3 4 5 2 6 1 9 -1
                     3
    Sample Output 1 :2
    Sample Input 2  :3 4 5 2 6 1 9 -1
                     0
    Sample Output 2 :3
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
def takeInput():
    inputList = [int(x) for x in input().split()]
    head = None
    tail = None
    for ele in inputList:
        if ele == -1:
            break
        newNode = Node(ele)
        
        if head is None:
            head = newNode
            tail = newNode
            
        else:
            tail.next = newNode
            tail = tail.next
            
    return head


def ithNode(head,i):
    current = head
    count = 0
    while current is not None:
        if count == i:
            return current.data
            
        else:
            count+=1
            current = current.next
    else:
        return " "
        
def printLinkedList(head):
    current = head
    while current is not None:
        print(str(current.data),"->",end= " ")
        current = current.next
    print("None")
        

head = takeInput()
i = int(input())
node =ithNode(head,i)
print(node)



