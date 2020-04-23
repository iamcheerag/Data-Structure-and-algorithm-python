# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:57:34 2020

@author: cheerag.verma
"""

#Program to implement queue using 2 stacks
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
        
    def enQueue(self,data):                              #O(1)
        self.stack1.append(data)
        #print(self.stack1)
        
    def deQueue(self):                                   #O(n)
        if self.stack1 is None:
            return -1   
        
        for i in range(len(self.stack1)-1):
            self.stack2.append(self.stack1.pop())
            
        if len(self.stack1)>0:
            data = self.stack1.pop()
        else:
            return -1
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        return data
    
    def size(self):
        return len(self.stack1)
    def isEmpty(self):
        return self.size() == 0

        
        
q = Queue()
q.enQueue(20)
q.enQueue(10)
q.enQueue(2)
q.enQueue(200)
print("size:",q.size())
print("isEmpty:",q.isEmpty())

while q.isEmpty() is False:
    print(q.deQueue())
q.size()
q.isEmpty()