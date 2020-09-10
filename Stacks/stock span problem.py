#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 08:23:42 2020

@author: Cheerag
"""
'''
try to identify the patter in the code, this problem is just a variation of NGL

eg:             10  100  80   90  60  20
                -1, -1, 100, 100, 90, 60
index of NGL    -1, -1,  1,   1,  3,  4  

actual index - index of NGL = result of stock span problem
'''

def stockSpanProblem(arr):
    stack  = []
    result = []
    
    
    for data in range(len(arr)):
        if len(stack) == 0:
            stack.append((arr[data],data))
            result.append(-1)
            
        else:
            while(len(stack)>0 and arr[data] > stack[-1][0]):
                stack.pop()
                
            if len(stack) == 0:
                result.append(-1)
                stack.append((arr[data],data))
                
                
                
            elif arr[data] < stack[-1][0]:
                stacktopElementIndex = stack[-1][1]
                result.append(stacktopElementIndex)
                stack.append((arr[data],data))
                
                
    return result
        
arr = [10,100,80,90,60,20]
result = stockSpanProblem(arr)

for idx in range(len(result)):
    result[idx]=idx-result[idx]

print(*result)

