# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:54:17 2020

@author: cheerag.verma
"""

def convertStrToInt(n):
    if len(n) == 1:
        return ord(n)-ord('0')
        
    smallList = convertStrToInt(n[1:])
    return smallList + (ord(n) - ord('0') * 10)
    
    
convertStrToInt('12')