# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:33:36 2020

@author: cheerag.verma
"""

"""
Given a string, compute recursively a new string where identical chars that are adjacent in the original string
are separated from each other by a "*".

Sample Input 1 :hello
Sample Output 1:hel*lo

"""

def PairStar(s,si):
    l = len(s)
    if si == l or si == l-1:
        return s[si]
    
    if s[si] == s[si+1]:
        return s[si]+ "*" + PairStar(s,si+1)
    else:
        return s[si] + PairStar(s,si+1)

PairStar('cheerag',0)

    
    
    