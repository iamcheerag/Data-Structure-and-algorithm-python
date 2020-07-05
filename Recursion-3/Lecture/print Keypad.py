# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 08:43:16 2020

@author: cheerag.verma
"""


def alphaCorresponding(rem):
    
    if rem == 2:
        char = "abc"
    elif rem == 3:
        char = "def"
    elif rem == 4:
        char = "ghi"
    elif rem == 5:
        char = "jkl"
    elif rem == 6:
        char = "mno"
        
    elif rem == 7:
        char = "pqrs"
    elif rem == 8:
        char = "tuv"
    elif rem == 9:
        char = "wxyz"
        
    return char

def keypad(n, output=""):
    if n == 0:
        print(output)
        return 
    
    rem = n % 10
    n = n //10
    alphaToKey = alphaCorresponding(rem)
    for alpha in alphaToKey:
        keypad(n, alpha+output)
    
keypad(23)
    
    