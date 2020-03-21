# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:07:46 2020

@author: cheerag.verma
"""
"""
Given an array of length N, you need to find and return the sum of all elements of the array.
Do this recursively.

Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces

Output Format :Sum
"""


def sumArray(a):
    n = len(a)
    if n == 1:      #base case
        return a[0]
    
    smallerOutput = a[1:]
    output = a[0] + sumArray(smallerOutput)
    return output 
    

a = [1,2,3,4,5,6]
sumArray(a)

