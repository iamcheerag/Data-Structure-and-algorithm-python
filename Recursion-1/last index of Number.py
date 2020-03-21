# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:08:09 2020

@author: cheerag.verma
"""
#This is from the last index
# =============================================================================
# def lastIndex(arr,x,si):
#     l = len(arr)
#     if si == l or si == l-1:
#         return -1
#     
#     elif arr[si] == x:
#         return l-si-1
#     
#     smallerList = lastIndex(arr[::-1],x,si+1)
#     return smallerList
# 
# n = int(input())
# arr = list(map(int,input().split()))
# x = int(input())
# print(lastIndex(arr[::-1],x,0))
# 
# =============================================================================

def lastIndex(arr,x):
    l = len(arr)
    if l == 0 :
        return -1
    
    smallList = arr[1:]
    output = lastIndex(smallList,x)

    if output != -1:
        return output+1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1
    
        
    
arr = [1,4,3,5,6]
x = 4
lastIndex(arr,x)