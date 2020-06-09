# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:21:02 2020

@author: cheerag.verma
"""
"""
K Largest Elements

You are given with an integer k and an array of integers that contain numbers in random order. Write a program to find k largest numbers from given array. You need to save them in an array and return it.
Time complexity should be O(nlogk) and space complexity should be not more than O(k).

    Order of elements in the output is not important.
        Input Format :
        Line 1 : Size of array (n)
        Line 2 : Array elements (separated by space)
        Line 3 : Integer k
        Output Format :
        k largest elements
        Sample Input :
        13
        2 12 9 16 10 5 3 20 25 11 1 8 6 
        4
        Sample Output :
        12
        16
        20
        25
"""

import heapq
def kSmallest(arr, k):
    li=[]
    count = 0
    for ele in arr:
        if count == k:
            break
        else:
            count+=1
            li.append(ele)
    
    heapq.heapify(li)
    for i in range(k,len(arr)):
        if arr[i] > li[0]:
            heapq.heapreplace(li, arr[i])
    return li
# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
for data in ans:
    print(data)