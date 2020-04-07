# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:19:18 2020

@author: cheerag.verma
"""
"""
Find the Unique Element

Given an integer array of size 2N + 1. In this given array, N numbers are present twice and one number is present only once in the array.
You need to find and return that number which is unique in the array.
Note : Given array will always contain odd number of elements.

Input format :
Line 1 : Array size i.e. 2N+1
Line 2 : Array elements (separated by space)

Output Format :
Unique element present in the array

Constraints :
1 <= N <= 10^6
"""



def FindUnique(arr):
    a = arr[0]
    for i in range(1,len(arr)):
        a = a ^ arr[i]
        print(a)
        
    return a


FindUnique([10,10,2,2,3,4,4])

#n=int(input())
#arr=list(int(i) for i in input().strip().split(' '))
#unique=FindUnique(arr)
#print(unique)

    