# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:31:16 2020

@author: cheerag.verma

Problem:  Check Palindrome (recursive)Check if a given String S is palindrome or not (using recursion).
          Return true or false.

Sample Input 1 : racecar

Sample Output 1: true

"""

def checkPalindrome(s,si,ei):
    if si >= ei:
        return True

    
    if s[si] == s[ei]:
        smallOutput = checkPalindrome(s,si+1,ei-1)
        return smallOutput
    else:
        return False
    
    
s = ''
result = checkPalindrome(s,0,len(s)-1)
if result:
    print("true")
else:
    print("false")









