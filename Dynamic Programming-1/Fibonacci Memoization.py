# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:24:49 2020

@author: cheerag.verma
"""

#normal fibanacci number with recursion 
# can we apply dp here?
# 1. Since it is optimal substructure -- 50% chances we can use dp
# 2. overlapping subproblem - yes we can apply dp for sure , cz we are calculating fib of same number more than 1.
# hence to apply dp it should be overlapping.

import time
start = time.time()

def fib(n):
    if n == 1 or n == 0 :
        return n 
    
    ans1 = fib(n-1)
    ans2 = fib(n-2)
    ans = ans1 + ans2
    return ans

n = int(input())
print(fib(n))
end = time.time()
print(end-start)



#using dp
import time
start = time.time()
def fib(n,dp):
    if n ==1 or n ==0:
        return n 
    
    if dp[n-1] == -1:
        ans1 = fib(n-1,dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]
        
        
    if dp[n-2] == -1:
        ans2 = fib(n-2,dp)
        dp[n-2] = ans2
    else:
        ans2 = dp[n-2]
        
    ans = ans1 + ans2
    return ans
    
    
n = int(input())
dp = [-1 for i in range(n+1)]

print(fib(n,dp))
end = time.time()
print(end-start)



#fib using iterative dynamic progg
import time
start = time.time()

def fibIterative(n):
    dpI = [0 for i in range(n+1)]
    
    dpI[0] = 0
    dpI[1] = 1
    i = 2
    while i <=n:
        dpI[i] = dpI[i-1] + dpI[i-2]
        i+=1
    
    return dpI[n]

n = int(input())
print(fibIterative(n))

end = time.time()
print(end-start)