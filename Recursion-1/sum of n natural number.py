# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:54:14 2020

@author: cheerag.verma
"""


def sumOfNaturalNumbers(n):
    if n == 0 :  #base case
        return 0
    smallOutput = sumOfNaturalNumbers(n-1)  # induction step donot think about this.
    return n + smallOutput

sumOfNaturalNumbers(10)


def sumofNaturalNumberWithoutRecursion(n):
    sum = 0 
    for i in range(n+1):
        sum +=i
    
    return sum 

sumofNaturalNumberWithoutRecursion(10)    