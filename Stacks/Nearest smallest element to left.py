#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:17:16 2020

@author: Cheerag
"""


def nearestSmallestElementToLeft(arr):
    stack  = []
    result = []
    for element in range(len(arr)):
        if len(stack) == 0:
            stack.append(arr[element])
            result.append(-1)
            
        else: #stack not empty
            while len(stack) > 0 and stack[-1] > arr[element]:
                stack.pop()
                
            if len(stack) == 0:
                result.append(-1)
                stack.append(arr[element])
                
                
            elif stack[-1] < arr[element]:
                result.append(stack[-1])
                stack.append(arr[element])
                
    return result


arr = list(map(int,input().split()))            
result = nearestSmallestElementToLeft(arr)
print(*result)
        
    