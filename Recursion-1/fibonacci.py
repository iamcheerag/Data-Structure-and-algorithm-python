# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:15:04 2020

@author: cheerag.verma
"""
# 1 1 2 3 5 8 13
# 0 1 1 2 3 5 8 13

def fibonacci(n):
    if n == 1 or n == 2:
        return 1 
    fib_n_1 = fibonacci(n-1) #induction step 
    fib_n_2 = fibonacci(n-2) #induction step
    
    output = fib_n_1 + fib_n_2
    return output


fibonacci(7)