# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 14:41:37 2020

@author: cheerag.verma
"""

import sys
def mcm(matrixArr,i,j,dp):
    if i ==j:
        return 0
    
    minCount = sys.maxsize
    for k in range(i,j):
        if dp[i][k] == -1:
            ans1 = mcm(matrixArr,i,k,dp)
            dp[i][k] = ans1
        else:
            ans1 = dp[i][k]
            
        if dp[k+1][j]:
            ans2 = mcm(matrixArr, k+1, j,dp)
            dp[k+1][j] = ans2
        else:
            ans2 = dp[k+1][j] 
        
        ans3 = matrixArr[i-1] * matrixArr[k] * matrixArr[j]
        
        count = ans1 + ans2 + ans3
        minCount = min(count,minCount)
    
    return minCount


sys.setrecursionlimit(100)

n = 4
arr =[10,15,20,25]
dp =[[-1 for j in range(n+1)] for i in range(n+1)]
print(mcm(arr,1,n-1,dp))


def mcm(matrixArr,i,j):
    if i ==j:
        return 0
    
    minCount = sys.maxsize
    for k in range(i,j):
        count = mcm(matrixArr,i,k)+ mcm(matrixArr, k+1, j)+ (matrixArr[i-1] * matrixArr[k] * matrixArr[j])
        #print(count)
        minCount = min(minCount,count)
            
    return minCount

## Read input as specified in the question.
## Print output as specified in the question.
import sys
def mcm(p,i,j,dp):
    if i == j:
        return 0
    minvalue = sys.maxsize
    for k in range(i,j):
        if dp[i][k] == -1:
            ans1 = mcm(p,i,k,dp)
            dp[i][k] = ans1 
        else:
            ans1 = dp[i][k]
        if dp[k+1][j] == -1:
            ans2 = mcm(p,k+1,j,dp)
            dp[k+1][j] = ans2
        else:
            ans2 = dp[k+1][j]
            
        mcost = p[i-1]*p[k]*p[j]
        currvalue = ans1 + ans2 + mcost
        minvalue = min(minvalue,currvalue)
        
    return minvalue
n = int(input())
p =list(int(i) for i in input().strip().split(' '))

n = len(p)-1
dp = [[ -1 for j in range(n+1)] for i in range(n+1)]
ans = mcm(p,1,n,dp)
print(ans)












