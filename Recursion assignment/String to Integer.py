# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:54:17 2020

@author: cheerag.verma
"""
"""
Write a recursive function to convert a given string into the number it represents. 
That is input will be a numeric string that contains only numbers, you need to convert the string into 
corresponding integer and return the answer.

Input format  :Numeric string (string, Eg. "1234")
Output format :Corresponding integer (int, Eg. 1234)
"""

def convertStrToInt(n):
    l = len(n)
    if len(n) == 1:
        return ord(n)-ord('0')
        
    first =  ord(n[0]) - ord('0')
    smallList = convertStrToInt(n[1:])
    return (first * (10 ** (l-1))) + smallList
    
convertStrToInt('12345')