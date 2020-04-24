# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:39:36 2020

@author: cheerag.verma
"""


import queue
def reverseQueue(q1):
    if q1.empty():
        return
    
    data = q1.get()
    reverseQueue(q1)
    return q1.put(data)
    
    
    

from sys import setrecursionlimit
setrecursionlimit(11000)
li = [int(ele) for ele in (input().split()[1:])]
q1 = queue.Queue()
for ele in li:
    q1.put(ele)
reverseQueue(q1)
while(q1.empty() is False):
    print(q1.get(),end= ' ')
    
    
    
