# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 00:04:41 2020

@author: cheerag.verma
"""


import queue
class StackUsingQueues:
    
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.count = 0
        
        
        
    def push(self,data):
        self.q1.put(data)
        self.count+=1

    def pop(self):
        if self.count == 0 :
            return -1
        
        for i in range(self.count-1):
            self.q2.put(self.q1.get())
         
        
        data = self.q1.get()
        
        self.count-=1
        
        for i in range(self.count):
            self.q1.put(self.q2.get())
        
        return data            
    
    def top(self):
        if self.count == 0 :
            return -1
        
        for i in range(self.count-1):
            self.q2.put(self.q1.get())
         
        
        data = self.q1.get()
        
        self.q2.put(data)
        
        for i in range(self.count):
            self.q1.put(self.q2.get())
        
        return data 
        

    def getSize(self):
        return self.count
    
  
s = StackUsingQueues()
s.push(2)
s.push(12)
s.push(22)
s.push(3)

s.pop()

print(s.getSize())

s.top()