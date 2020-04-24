# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 04:04:10 2020

@author: cheerag.verma
"""
class Stack:
    def __init__(self):
        self.__input = []

    def push(self,data):
        self.__input.append(data)
        
    def pop(self):
        if self.isEmpty() is True:
            return "Empty Array Nothing to Pop"
        return self.__input.pop()
        
    def isEmpty(self):
        return self.size() == 0
        
    def size(self):
        return len(self.__input)
    
    def top(self):
        if self.isEmpty() is True:
            return "Empty array"
             
        index = len(self.__input)-1
        return self.__input(index)
        


s = Stack()
li = list(map(int,input().split()))
for i in range(len(li)):
    s.push(li[i])

while s.isEmpty() is False:
    print("Poped Element:",s.pop())

print(s.pop())
print("Size of the element:",s.size())
print("Is array Empty:",s.isEmpty())
print("Element on the top:",s.top())
