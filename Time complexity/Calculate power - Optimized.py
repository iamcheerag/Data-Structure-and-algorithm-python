# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:22:35 2020

@author: cheerag.verma
"""

def power(x,n):
    if n == 0:
        return 1 
    
    smallPower = power(x,n//2)
    if n % 2 == 0:
        return smallPower * smallPower
    else:
        return x * smallPower*smallPower
    
power(3,4)
