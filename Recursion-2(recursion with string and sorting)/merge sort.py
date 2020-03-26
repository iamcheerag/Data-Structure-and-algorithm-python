# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:47:13 2020

@author: cheerag.verma
"""

def merge(left,right,a):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):  #yeh condition when both are of same length
        if left[i] < right[j]:
            a[k] = left[i]
            k+=1
            i+=1
         
        else:
            a[k] = right[j]
            k+=1
            j+=1
            
    
    while i < len(left):  # yeh agr left wale mein kuch remaining ho
        a[k] = left[i]
        k+=1
        i+=1

    while j < len(right):  #yeh agar left wale mein kuch remaning ho
        a[k] = right[j]
        k+=1
        j+=1



def mergeSort(a):
    if len(a) ==0 or len(a) == 1:  #base case 
        return 
    
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]
    
    mergeSort(left)             #yeh tab tak left calculate karge jab tak single element na mile
    mergeSort(right)            #similarly jab tak right ka single element na mile tab tak yeh bhi calc hota rhega
    
    merge(left,right,a)         #as soon as this return comes merge mein chla jayega woh

a= [8,4,2,5,66,53,21]
mergeSort(a)

