# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:41:45 2020

@author: cheerag.verma
"""
class Queue:
    def __init__(self):
        self.input = []
        self.front = 0
        self.rear = 0
        
    def enQueue(self,data):
        self.input.append(data)
        self.rear = self.rear +1
        #return self.input
        
        
    def deQueue(self):
        if self.isEmpty():
            return -1
        data = self.input[self.front]
        self.front = self.front + 1
        self.rear = self.rear -1
        return data
        
    def size(self):
        return self.rear
        
    def frontElement(self):
        if self.isEmpty():
            return -1
        return self.input[self.front]
        
    def isEmpty(self):
        return self.size() == 0


queue = Queue()
queue.enQueue(20)
queue.enQueue(10)
queue.enQueue(2)
queue.enQueue(3)

while queue.isEmpty() is False:
    print(queue.deQueue())

print(queue.size())
print(queue.frontElement())