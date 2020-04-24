# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:02:49 2020

@author: cheerag.verma
"""

import queue
s = []
def reverseFirstK(q,si,k,n):
    if q.empty():
        return 
    if si == k:
        for i in range(n-k):
            s.append(q.get())
        return q
    
    data = q.get()
    reverseFirstK(q,si+1,k,n)

    return q.put(data)



q = queue.Queue()
q.put(2)
q.put(12)
q.put(22)
q.put(32)
q.put(42)
n=5
reverseFirstK(q,0,3,n)
for i in s:
    q.put(i)
while q.qsize()>0:
    print(q.get())
