# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:10:29 2020

@author: cheerag.verma
"""


def minimumBracketReversal(string):    
    l = len(string)
    stackA=[]
    stackB=[]
    if l == 0:
        return 0
    
    if l % 2 != 0:
        return -1
    
    for i in string:
        if i in "{":
            stackA.append(i)
        else:
            stackB.append(i)
        
    lenStackA = len(stackA)
    mid = l//2
    result = lenStackA-mid
    if result < 1:
        result = result *(-1)
    
    return result

string = "  {}   {}   {{"
string = string.replace(" ","")
result = minimumBracketReversal(string)
print(result)