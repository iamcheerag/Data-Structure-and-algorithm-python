# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:18:39 2020

@author: cheerag.verma
"""

def replacePi(s):
    if len(s) == 0 or len(s) == 1:   # it basically means lenght will be 2 definately
        return s
    
    if s[0] == 'p' and s[1] == 'i':
        smallOutput = replacePi(s[2:])
        return '3.14' + smallOutput
    else:
        smallOutput = replacePi(s[1:])
        return s[0]+ smallOutput
    
s = 'avcpicdpi'
replacePi(s)
    