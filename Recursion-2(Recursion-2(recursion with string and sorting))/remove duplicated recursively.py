# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:09:36 2020

@author: cheerag.verma
"""

"""
Problem : Given a string S, remove consecutive duplicates from it recursively.

Sample Input  : aabccba

Sample Output : abcba

"""

def removeConsecutiveDuplicates(s):
    if len(s) == 0 or len(s) == 1:
        return s
    
    if s[0] == s[1]:
        smallOutput = removeConsecutiveDuplicates(s[1:])
        return  smallOutput
    else:
        smallOutput = removeConsecutiveDuplicates(s[1:])
        return s[0] + smallOutput


string = 'cheerag'
print(removeConsecutiveDuplicates(string))