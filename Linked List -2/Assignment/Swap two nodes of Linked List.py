# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 18:09:05 2020

@author: cheerag.verma
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None
        
        
        
def createLL(arr):
    if len(arr) == 0:
        return None
    
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
        
    return head


def swapNode(head,i,j):
    if j>i:
        i,j = j,i
    
    
    if head is None:
        return None
    
    
    currPtr = head
    currPtr2 = head
    icount = 0
    jcount = 0
 
    
    while currPtr :
        if icount == i:
            nextPtr = currPtr.next
            break
        else:
            prevPtr = currPtr
            currPtr= currPtr.next
            icount+=1
            
            
    while currPtr2:
        if jcount == j:
            nextPtr2 = currPtr2.next
            break
        else:
            prevPtr2 = currPtr2 
            currPtr2= currPtr2.next
            jcount += 1

    temp = currPtr2
    
    
    if i == 0 and currPtr.next == currPtr2:
        
        currPtr.next = currPtr.next.next
        head = temp
        temp.next = currPtr
   
    elif i == 0:
        prevPtr2.next= currPtr
        currPtr.next = nextPtr2
        head = temp
        temp.next = nextPtr
    
    elif currPtr.next == currPtr2:    #when i and j are consecutives
        currPtr.next = nextPtr2
        prevPtr.next = temp
        temp.next = currPtr
        
    else:
        prevPtr2.next = currPtr   
        currPtr.next = nextPtr2
        prevPtr.next = temp
        temp.next = nextPtr
    
    return head

def printLL(head):
    current = head
    while current is not None:
        print(current.data,end= " ")
        current = current.next
        
arr = [int(x) for x in input().split()]
head = createLL(arr[:-1])
li = list(map(int,input().split()))
head = swapNode(head,li[0],li[1])
printLL(head)




        
    
    
    