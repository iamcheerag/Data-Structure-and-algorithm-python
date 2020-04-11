# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 08:38:23 2020

@author: cheerag.verma
"""

def rotate(arr,x):
    right_arr = arr[x:]
    left_arr = arr[:x]
    
    new_arr = right_arr + left_arr
    
    return new_arr
    
    
arr = list(map(int,input().split()))
d = int(input())
rotate(arr,d)

    