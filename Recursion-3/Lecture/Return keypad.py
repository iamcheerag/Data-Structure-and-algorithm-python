# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:27:14 2020

@author: cheerag.verma



Return Keypad

Given an integer n, using phone keypad find out all the possible strings that can be made using digits of input n.
Note : The order of strings are not important.
    Input Format :
    Integer n
    Output Format :
    All possible strings in different lines
    Constraints :
    1 <= n <= 10^6

"""

def keypad(n):
    if n == 0:
        output = []
        output.append("")
        return output
    
    smalloutput = keypad(n//10)
    rem = n%10
        
    
    if rem == 2:
        char = "abc"
    if rem == 3:
        char = "def"
    if rem == 4:
        char = "ghi"
    if rem == 5:
        char = "jkl"
    if rem == 6:
        char = "mno"
        
    if rem == 7:
        char = "pqrs"
    if rem == 8:
        char = "tuv"
    if rem == 9:
        char = "wxyz"
    
    result = []
    for data in char:
        for ele in smalloutput:
            result.append(ele+data)
        
    return result


print(keypad(23))
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    