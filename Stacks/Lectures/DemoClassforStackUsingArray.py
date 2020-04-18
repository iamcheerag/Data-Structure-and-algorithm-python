# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:30:45 2020

@author: cheerag.verma
"""

from StackUsingArray import Stack

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.top())
print(s.size())
print(s.isEmpty())

while s.isEmpty() is False:
    print(s.pop())
    
    
print(s.top())