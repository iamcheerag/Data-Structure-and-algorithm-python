# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:13:40 2020

@author: cheerag.verma
"""

def checkAB(s,si):
    l = len(s)
    if si == l or si == l-1: #base case
        return True

    if s[si] == "a" :
       if (s[si+1] == "a" or s[si+1] == " ") :
           return checkAB(s,si+1)
       elif (s[si+1] =="b" and s[si+2] == "b"):
           return checkAB(s,si+2)
       else:
           return False
      
    if s[si] == "b":
        if s[si+1] == " " or s[si+1] == "a":
            return checkAB(s,si+1)
        else:
            return False
        

s = "ab"
if s[0] == 'a' or " ":
    result = checkAB(s,0)
    if result:
        print("true")
    else:
        print("false")
else:
    print("false")
        