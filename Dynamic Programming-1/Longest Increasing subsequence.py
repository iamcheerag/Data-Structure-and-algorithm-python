# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:24:39 2020

@author: cheerag.verma
"""

# using dp array (Recursive)
def longestIncreasingSubseq(arr,i,n,dp):
    
    if i == n:
        return 0,0
    
    includingMax = 1
    for j in range(i+1,n):
        if arr[j] >= arr[i]:
            if dp[j] == -1:
                ans = longestIncreasingSubseq(arr, j, n,dp)
                dp[j] = ans
                includingNum = ans[0]
                
            else:
                includingNum = dp[j][0]
                
            includingMax = max(includingMax,1+includingNum)
        
    if dp[i+1] == -1:
        ans = longestIncreasingSubseq(arr, i+1, n,dp)
        dp[i+1] = ans
        excludingNum = ans[1]
    else:
        excludingNum = dp[i+1][1]      
        
    overallMax = max(includingMax,excludingNum)
    return includingMax,overallMax
        
arr = [6,3,1,2,7,0,8,8]
n = len(arr)
dp = [-1 for i in range(n+1)]
print(longestIncreasingSubseq(arr, 0, len(arr),dp)[1])











# Using Iterative Dynamic Programming


def LisIterative(arr,n):
    dp = [[0 for j in range(2)] for i in range(n+1)]
    
    for i in range(n-1,-1,-1):
        including_max = 1
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                including_max = max (including_max , 1 + dp[j][0])
        dp[i][0] = including_max
        
        excluding_max = dp[i+1][1] # just next element in the right direction
        overall_max = max(including_max,excluding_max)
        dp[i][1] = overall_max
        
    return dp[0][1]
                

n = 8
arr =  [6,3,1,2,7,0,8,8]
LisIterative(arr, n)
    




