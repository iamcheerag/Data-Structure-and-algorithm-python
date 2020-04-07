# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:04:56 2020

@author: cheerag.verma
"""

"""
Array Equilibrium Index

Find and return the equilibrium index of an array. Equilibrium index of an array is an index i such that the 
sum of elements at indices less than i is equal to the sum of elements at indices greater than i.
Element at index i is not included in either part.
If more than one equilibrium index is present, you need to return the first one. And return -1 if no 
equilibrium index is present.

Input format :
Line 1 : Size of input array
Line 2 : Array elements (separated by space)

Constraints:
Time Limit: 1 second
Size of input array lies in the range: [1, 1000000]
"""

def equilibriumIndex(arr):
    Sum = sum(arr[0:])
    i = 0
    left_s = 0
    while i < len(arr): 
        s = Sum-arr[i]   #substract element from the sum
        if  s == left_s:
            print(i)
            break
        left_s = left_s + arr[i]
        Sum = s
        i+=1
    else:
        print(-1)

arr=[5,1,3,2,4,4]
equilibriumIndex(arr)