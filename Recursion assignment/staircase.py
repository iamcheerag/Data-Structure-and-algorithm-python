# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:37:40 2020

@author: cheerag.verma
"""

def stairCase(n):
    
    if n == 0 or n == 1:
        return 1
    
    elif n == 2:
        return  2
    
    else:
        return stairCase(n-1) + stairCase(n-2) + stairCase(n-3)
    

stairCase(4)