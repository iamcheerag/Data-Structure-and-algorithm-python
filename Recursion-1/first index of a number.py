# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:54:31 2020

@author: cheerag.verma
"""

def firstOccurance(arr,x,si):
    l = len(arr)
    if si == l-1 or si == l:   #si== l (no element to point cz si start from 0 toh yeh cross kar jayega l ko)
        return False
    elif arr[si] == x:
        return si
    smallList = firstOccurance(arr,x,si+1)
    return smallList

arr = [1,2,2,4,5,4]
firstOccurance(arr,4,0)