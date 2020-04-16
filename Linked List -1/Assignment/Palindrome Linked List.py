# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 00:36:02 2020

@author: cheerag.verma
"""
"""
Palindrome LinkedList
Send Feedback
Check if a given linked list is palindrome or not. Return true or false.
Indexing starts from 0.
Input format : Linked list elements (separated by space and terminated by -1)

Sample Input 1 :
    9 2 3 3 2 9 -1
Sample Output 1 :
    true
Sample Input 2 :
    0 2 3 2 5 -1
Sample Output 2 :
    false
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
def createLL(arr):
    if len(arr)== 0:
        return 
    
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    
    return head

def reverseLL(head):
    current = head
    prev=None
    
    while current is not None:
        next_ = current.next 
        current.next = prev
        prev = current
        current = next_
    head = prev
    
    return head
def Palindrome(head1,head2):
    currentOriginal = head1
    currentReverse  = head2
    
    while currentOriginal is not None:
        if currentOriginal.data !=currentReverse.data:
            return False
        else:
            currentOriginal= currentOriginal.next
            currentReverse = currentReverse.next
    
    else:
        return True
    
    
def printLL(head):
    current = head
    while current is not None:
        print(current.data,end= " ")
        current = current.next
    print()
        
arr = [int(x) for x in input().split()]
head1 = createLL(arr[:-1]) #creating new linkedlist
head2 = createLL(arr[:-1]) #creating new linkedlist
#printLL(head1)
head2 = reverseLL(head2)
#printLL(head2)
result = Palindrome(head1,head2)
if result:
    print("true")
else:
    print("false")