# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:18:38 2020

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
  
# def calcLenght(head):
#     if head.next is None:
#         return 1
#     #smallHead = calcLenght(head.next)
    
#     return 1 + calcLenght(head.next)
    

def calcLenght(head):
    count = 0
    current = head
    while current is not None:
        current = current.next
        count+=1
    return count
    
def midPointLL(head):
    if head.next is None:
        return head.data
    
    l = calcLenght(head)
    current = head
    mid = l//2
    count = 1
    while current is not None:
        if count == mid:
            break
        else: 
            current = current.next
            count+=1
        
    if l%2 ==0 :
            return current.data
    else:
        return current.next.data
        
    
def midPointLL2(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
            
    return slow

arr = list(map(int,input().split()))
head = createLL(arr[:-1])
#node = midPointLL(head)
print("using slow and fast pointer")
node = midPointLL2(head)
if node:
    print(node.data)


