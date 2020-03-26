# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:00:02 2020

@author: cheerag.verma
"""

"""
Problem:  Given two integers m & n, calculate and return their multiplication using recursion. 
          You can only use subtraction and addition for your calculation. No other operators are allowed.
          Input format : m and n (in different lines)

Sample Input :  3 
                5

Sample Output - 15

"""

def multiplication(m,n):
    if n == 1 or m == 0:
        return m
    
    smallList = multiplication(n-1,m)   # induction step 
    return m + smallList


#m=int(input())
#n = int(input())
multiplication(0,0)