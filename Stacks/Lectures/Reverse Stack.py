# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:36:14 2020

@author: cheerag.verma
"""
"""
Reverse Stack

Reverse a given Stack with the help of another empty stack. Two stacks will be given. Out of which first contains some integers and second one is empty. You need to reverse the first one using second stack. Change in the given first stack itself.
Note : You don't need to print or return the stack, just reverse the given stack and it will be printed internally.
    Input format :
    Line 1 : Size of Stack
    Line 2 : Stack elements (separated by space)
    Sample Input 1 :
    4 
    1 2 3 4     (4 is at top)
    Sample Output 1 :
    1 2 3 4    (1 is at top)
"""


def reverseStack(s1,s2):
    if len(s1) == 1:
        return s1
    
    for i in range(len(s1)-1):
        s2.append(s1.pop())
     
    ele = s1.pop()
    
    for i in range(len(s2)):
        s1.append(s2.pop())
    
    reverseStack(s1,s2)
    return s1.append(ele)
    
    
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []
reverseStack(s1,s2)
while(len(s1) !=0):
    print(s1.pop(),end= ' ')





