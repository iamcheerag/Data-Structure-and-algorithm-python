# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 04:37:33 2020

@author: cheerag.verma
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class StackUsingLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0
        
    def push(self,element):
        newNode = Node(element)
        newNode.next = self.__head
        self.__head = newNode
        self.__count = self.__count +1
        
    def pop(self):
        if self.isEmpty() is True:
            return "Nothing to Pop"
        popedElement = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count -1
        return popedElement
        
    def size(self):
        return self.__count
        
    def isEmpty(self):
        return self.__count == 0
        
    def top(self):
        if self.isEmpty() is True:
            return "Nothing on the top"
        topElement = self.__head.data
        return topElement
        
        
s = StackUsingLinkedList()
s.push(10)
s.push(20)
# #li = list(map(int,input().split()))
# for i in range(len(li)):
#     s.push(li[i])

# while s.isEmpty() is False:
#     print("Poped Element:",s.pop())

print(s.pop())
print("Size of the element:",s.size())
print("Is array Empty:",s.isEmpty())
print("Element on the top:",s.top())
        
        