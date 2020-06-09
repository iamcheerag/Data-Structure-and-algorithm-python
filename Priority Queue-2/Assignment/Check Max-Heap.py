# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:28:08 2020

@author: cheerag.verma
"""
"""
Check Max-Heap

    Given an array of integers, check whether it represents max-heap or not.
    Return true or false.
        Input Format :
            Line 1 : An integer N i.e. size of the array
            Line 2 : N integers which are elements of the array, separated by spaces
        Output Format :
            true if it represents max-heap and false if it is not a max-heap
        Constraints :
            1 <= N <= 10^5
"""



def checkMaxHeap(arr):
    n = len(arr)
    
    for i in range(n//2-1,-1,-1):
        parentIndex = i
        
        leftChildIndex  = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2
        
        if leftChildIndex < n and arr[parentIndex] < arr[leftChildIndex]:
            return False
        
        if rightChildIndex < n and arr[parentIndex] < arr[rightChildIndex]:
            return False
        
         
    return True


# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
