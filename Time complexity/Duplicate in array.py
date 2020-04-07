# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:52:10 2020

@author: cheerag.verma
"""

"""
Duplicate in array

Given an array of integers of size n which contains numbers from 0 to n - 2. Each number is present at least once. That is, if n = 5, numbers from 0 to 3 is present in the given array at least once and one number is present twice. You need to find and return that duplicate number present in the array.
Assume, duplicate number is always present in the array.

Input format :
Line 1 : Size of input array
Line 2 : Array elements (separated by space)

Output Format :
Duplicate element
"""

def MissingNumber(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] ^ arr[i+1] ==0:
            return arr[i]

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=MissingNumber(arr)
print(ans)