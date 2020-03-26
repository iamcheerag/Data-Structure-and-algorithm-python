# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:11:27 2020

@author: cheerag.verma
"""

"""
Write a recursive function that returns the sum of the digits of a given integer.
Sample Input :  12345

Sample Output : 15

"""


def sumofdigits(n):
    if n==0 or n ==1:   #base case : when single digit or no digit
        return n
    smallList = sumofdigits(n//10)
    return n%10 + smallList
    
    
n = int(input())
sumofdigits(n)