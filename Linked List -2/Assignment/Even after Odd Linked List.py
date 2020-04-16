# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:24:06 2020

@author: cheerag.verma
"""
"""
Even after Odd LinkedList

Arrange elements in a given Linked List such that, all even numbers are placed after odd numbers. Respective order of elements should remain same.
Note: Input and Output has already managed for you. You don't need to print the elements, instead return the head of updated LL.
    Input format:
    Linked list elements (separated by space and terminated by -1)
    Output format:
    Print the elements of updated Linked list. 
    
    Sample Input 1 :
    1 4 5 2 -1
    Sample Output 1 :
    1 5 4 2 
    
    Sample Input 2 :
    1 11 3 6 8 0 9 -1
    Sample Output 2 :
    1 11 3 9 6 8 0

"""






class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
    
    if head.next is None:
        return head
    
    odd_head  = None
    odd_tail  = None
    even_head = None
    even_tail = None
    
    current =  head 
    while current is not None:
        if current.data % 2 !=0 : # odd
            
            if odd_head is None:
                odd_head = current
                odd_tail = current
                
            else:
                odd_tail.next = current
                odd_tail = odd_tail.next
            
            current = current.next
            
        
        else:    #even
            if even_head is None:
                even_head = current
                even_tail = current
            
                
            else:
                even_tail.next = current
                even_tail = even_tail.next
            
            current = current.next

    
    if odd_tail:
        odd_tail.next = even_head
    
    if even_tail:
        even_tail.next = None
    else:
        odd_tail.next = None
    
    
    if odd_head is None:
        return even_head
    else:
        return odd_head
    
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

arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = arrange_LinkedList(l)

printll(l)
