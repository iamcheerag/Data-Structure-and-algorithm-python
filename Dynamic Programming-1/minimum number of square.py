<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 11:29:12 2020

@author: cheerag.verma
"""

import sys
import math
def minNumberSquare(n):
    ans = sys.maxsize
    if n == 0:
        return 0

    for i in range(1,int(math.sqrt(n))+1):
        minAns = 1+ minNumberSquare(n-(i**2))
        ans = min(minAns,ans)
        
    return ans


print(minNumberSquare(41))
        
#=================================================================

import sys
import math
def minNumberSquare(n,dp):
    ans = sys.maxsize
    if n == 0:
        return 0

    for i in range(1,int(math.sqrt(n))+1):
        if dp[n-(i**2)] == -1:
            minAns = 1 + minNumberSquare(n-(i**2),dp)
            dp[n-(i**2)] = minAns
        else:
            minAns = dp[n-(i**2)]
            
        ans = min(minAns,ans)
        
    return ans
        
sys.setrecursionlimit(110000)  # to pass test cases
n = int(input())
dp = [-1 for i in range(n+1)]
print(minNumberSquare(n,dp))
=======
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 11:29:12 2020

@author: cheerag.verma
"""

import sys
import math
def minNumberSquare(n):
    ans = sys.maxsize
    if n == 0:
        return 0

    for i in range(1,int(math.sqrt(n))+1):
        minAns = 1+ minNumberSquare(n-(i**2))
        ans = min(minAns,ans)
        
    return ans


print(minNumberSquare(41))
        
#=================================================================

import sys
import math
def minNumberSquare(n,dp):
    ans = sys.maxsize
    if n == 0:
        return 0

    for i in range(1,int(math.sqrt(n))+1):
        if dp[n-(i**2)] == -1:
            minAns = 1 + minNumberSquare(n-(i**2),dp)
            dp[n-(i**2)] = minAns
        else:
            minAns = dp[n-(i**2)]
            
        ans = min(minAns,ans)
        
    return ans
        
sys.setrecursionlimit(110000)  # to pass test cases
n = int(input())
dp = [-1 for i in range(n+1)]
print(minNumberSquare(n,dp))
>>>>>>> e9f61ce6d8dd9e8eeb45fc231f5eaebe06d511c8
        