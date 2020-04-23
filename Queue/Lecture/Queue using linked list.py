# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:21:30 2020

@author: cheerag.verma
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class QueueUsingLL:
  
    def __init__(self):
        self.__head = None
        self.__count = 0
        self.__tail = None
    
    def enqueue(self,data):
        if self.__head is None:
            self.__head = Node(data)
            self.__tail = self.__head
        else:
            self.__tail.next = Node(data)
            self.__tail = self.__tail.next
        self.__count+=1
        
            
    def dequeue(self):
        if self.__head is None:
            return -1
        data = self.__head.data
        self.__head = self.__head.next
        self.__count-=1
        return data
    
    def front(self):
        if self.isEmpty():
            return -1
        return self.__head.data
        
    def isEmpty(self):
        return self.getSize() == 0
       
    
    def getSize(self):
        return self.__count
        
    
q = QueueUsingLL()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)


q.dequeue()
q.getSize()
q.isEmpty()
q.front()