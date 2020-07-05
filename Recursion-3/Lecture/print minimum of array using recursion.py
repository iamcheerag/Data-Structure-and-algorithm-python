# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 07:28:37 2020

@author: cheerag.verma
"""

import sys
def minNum(arr):
    if len(arr) == 0:
        return sys.maxsize
    
    minFromSmallerList = minNum(arr[1:])
    ans = min(arr[0],minFromSmallerList)
    return ans

result = minNum([3,1,2,3,4,5])
print(result)





def printMin(arr,ans=sys.maxsize):
    if len(arr) == 0:
        print(ans)
        return
    
    ans = min(ans,arr[0])
    printMin(arr[1:],ans)
    
printMin([3,1,2,3,4,5])