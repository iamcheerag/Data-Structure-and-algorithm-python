# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:13:40 2020

@author: cheerag.verma
"""

     
def checkAB(s)  :
    
    if len(s) == 0:
        return True
    
    if len(s) == 1:
        if s[0] == 'a':
            return True
        else:
            return False
    
    if len(s) ==2:
        if s[0] == 'a' and s[1] == 'a':
            return True
        else:
            return False
    
    if len(s)>2:
        if s[0] == 'a' and s[1] == 'b' and s[2] =='b':  #induction hypothesis
            smallresult = checkAB(s[3:])
        elif s[0] == "a" and s[1] == "a":
            smallresult = checkAB(s[1:])
        else:
            return False
        return smallresult

s= "abb"
result = checkAB(s)
if result:
    print("true")
else:
    print("false")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    