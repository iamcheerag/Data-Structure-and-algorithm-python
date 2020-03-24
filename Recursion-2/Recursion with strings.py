# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:25:18 2020

@author: cheerag.verma
"""


#Iterative solution
str = 'Cheerag'
strNew = ''
for i in str:
    if i == 'e':
        strNew = strNew + 'i' 
    else:
        strNew = strNew+i
        
        

#Recursive solution
def recursionString(s,x,y):
    if len(s) == 0:
        return s

    smallerList = s[1:]
    smallOutput = recursionString(smallerList,x,y)
    if s[0] == x:
        return y + smallOutput
    else:
        return s[0] +  smallOutput 
    
    return smallOutput

s = "Cheerag"
recursionString(s,'e','i')