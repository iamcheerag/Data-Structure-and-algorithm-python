# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:36:33 2020

@author: cheerag.verma
"""

def binarySearch(arr,start,end,searchElement):

    if start > end :
        return -1
    
    mid = (start + end )//2
    
    if searchElement == arr[mid]:
        print('Element found at ', mid)
        
    elif arr[mid] > searchElement:  #element in left half
        return binarySearch(arr,start,mid-1,searchElement)
    
    elif arr[mid] < searchElement:
        return binarySearch(arr,mid+1,end,searchElement)
    
    
arr = [10,20,40,50,60,70,80,100]
n = len(arr)
start = 0
end = n-1        
binarySearch(arr,start,end,60)