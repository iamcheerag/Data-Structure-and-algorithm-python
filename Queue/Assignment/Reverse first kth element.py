# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:02:49 2020

@author: cheerag.verma
"""
"""
Reverse first K elements

Given a queue and an integer k, reverse first k elements. Return the updated queue.
Do the problem in O(n) complexity.
Input Format :
    Line 1 : Integer N, Size of Queue
    Line 2 : Queue Elements (separated by space)
    Line 3 : Integer k
Output Format:
    Updated Queue elements
Contraints :
    1<= N <=10000
Sample Input 1:
    5
    1 2 3 4 5
    3
Sample Output 1:
    3 2 1 4 5

Sample Input 2:
    7
    3 4 2 5 6 7 8
    7
Sample Output 2:
    8 7 6 5 2 4 3
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
