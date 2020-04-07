# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:53:01 2020

@author: cheerag.verma
"""

"""
Tip : for array problems sort the array first"""



def binarySearch(arr,start,end,searchElement):

    if start > end :
        return -1
    
    mid = (start + end )//2
    
    if searchElement == arr[mid]:
        print(arr[mid])
        return arr[mid]
        
    elif arr[mid] > searchElement:  #element in left half
        return binarySearch(arr,start,mid-1,searchElement)
    
    elif arr[mid] < searchElement:
        return binarySearch(arr,mid+1,end,searchElement)

    
def arrayIntersection(arr1,arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    
    if l1>=l2:
        arr2.sort()

        for i in arr1:
            binarySearch(arr2,0,len(arr2)-1,i)
    else:
        arr1.sort()

        for i in arr2:
            binarySearch(arr1,0,len(arr1)-1,i)


def removeDuplicates(arr):
    xor = 0
    for i in range(len(arr)):
        xor^=arr[i]
        print(xor)
    
    for i in range(len(arr)):
        arr[i] = xor^arr[i]
    
    return arr


arr = [2,4,5,4,6,7]
arr2=  [7,9,77,5]
arr2 = removeDuplicates(arr)
arrayIntersection(arr1, arr2)

        
#---------------------------------------------------------------------------------

    
def arrayIntersection(l1,l2):
    l1.sort()
    l2.sort()
    i = 0
    j = 0
    while (i < len(l1)):
        
        while(j< len(l2)):
            
            if l1[i] >= l2[j]:
                
                if l1[i] != l2[j]:
                    j+=1
                
                elif l1[i] == l2[j]:
                    print(l1[i])
                    j+=1
                    break
                    
            else:
                i+=1
        
        i+=1
        
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
arrayIntersection(arr1, arr2)
    
#---------------------------------------------------------------------------------

def arrayIntersection(arr1,arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    
    while i < len(arr1) and j <len(arr2):
        if arr1[i] == arr2[j]:
            print(arr1[i])
            i +=1
            j+=1
        
        elif arr1[i] > arr2[j]:
            j+=1
        else:
            i+=1

n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
arrayIntersection(arr1, arr2)