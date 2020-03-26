# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:30:18 2020

@author: cheerag.verma
"""
"""
Given an integer n, count and return the number of zeros that are present in the given integer using recursion.

Sample Input    : 10204
Sample Output   :     2

"""
def countZero(n):
    if n== 0 :
        return 1
    
    if n == 1:
        return 0 
    
    if n //10 == 0:
        return 0
    
    smallList = countZero(n//10)
    print(smallList)
    if n % 10 == 0:
        return smallList +1
    else:
        return smallList
    
    
countZero(30452032)