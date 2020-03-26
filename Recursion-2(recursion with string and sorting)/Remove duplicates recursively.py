# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:30:45 2020

@author: cheerag.verma
"""

"""
Given a string S, remove consecutive duplicates from it recursively.

Sample Input :  aabccba

Sample Output : abcba

Constraints :
1 <= Length of String S <= 10^3

"""


def removeConsecutiveDuplicates(s):
    if len(s) == 0 or len(s) == 1:
        return s
    
    if s[0] == s[1]:
        smallOutput = removeConsecutiveDuplicates(s[1:])
        return smallOutput
    else:
        smallOutput = removeConsecutiveDuplicates(s[1:])
        return s[0] + smallOutput
# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
