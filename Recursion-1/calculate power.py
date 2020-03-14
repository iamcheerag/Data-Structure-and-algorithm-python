# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:05:51 2020

@author: cheerag.verma
"""

def power(x,n):
    if n == 0:
        return 1
    smallOutput = power(x,n-1)
    return x * smallOutput


x,n = list(map(int,input().split(" ")))

result = power(x,n)
print(result)
    
    