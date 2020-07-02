<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:44:44 2020

@author: cheerag.verma
"""
############################################### RECURSIVE PROGRAMMING ################################
import sys
def costFunction(costArr,m,n,i,j):
    
    #base case
    if i>=m or j>=n:
        return sys.maxsize
    #special case
    if i == m-1 and j == n-1:
        return costArr[i][j]
    
    ans1 = costFunction(costArr, m, n, i+1, j)
    ans2 = costFunction(costArr, m, n, i, j+1)
    ans3 = costFunction(costArr, m, n, i+1, j+1)
    
    result = costArr[i][j] + min(ans1,ans2,ans3)
    return result

    
m = 3
n = 3
#costArr = [[int(j) for j in input().split()] for i in range(m)]
costArr = [[5,1,19],[2,12,6],[7,4,9]]
print(costFunction(costArr,m,n,0,0))

############################################### RECURSIVE DYNAMIC PROGRAMMING ################################
import sys
def costFunction(costArr,m,n,i,j,dp):
    
    #base case
    if i>= m or j>= n:
        return sys.maxsize
    
    #special case to handle last grid
    if i == n-1 and j == m-1: 
        return costArr[i][j]
    
    # if i == n-1 or j == n-1:
    #     return sys.maxsize
    
    if dp[i+1][j] == sys.maxsize:
          ans1 = costFunction(costArr, m, n, i+1, j, dp)
          dp[i+1][j] = ans1
    else:
        ans1 = dp[i+1][j]

    if dp[i][j+1] == sys.maxsize:
        ans2 = costFunction(costArr, m, n, i, j+1, dp)
        dp[i][j+1] = ans2
    else:
        ans2 = dp[i][j+1]

    if dp[i+1][j+1] == sys.maxsize:
        ans3 = costFunction(costArr, m, n, i+1, j+1, dp)
        dp[i+1][j+1] = ans3
    else:
        ans3 = dp[i+1][j+1]
    
    print(ans1,ans2,ans3)
    result = costArr[i][j] + min(ans1,ans2,ans3)
    return result

    
#m = int(input())
m = 2
#n = int(input())
n = 2
costArr = [[5,1],[6,8]]
dp = [[sys.maxsize for j in range(n+1)]for i in range(m+1)]
print(costFunction(costArr,m,n,0,0,dp))

#m,n = [int(input) for input in input().split()]

import sys
def minCostIter(arr,m,n):
    ans1 = sys.maxsize
    ans2= sys.maxsize
    ans3 = sys.maxsize
    dp = [[sys.maxsize for j in range(m+1)]for i in range(n+1)]
    for row in range(m-1,-1,-1):
        for col in range(n-1,-1,-1):
            if row == m-1 and col == n-1:
                dp[row][col] = arr[row][col]
            else:
                ans1 = dp[row+1][col]
                ans2 = dp[row][col+1]
                ans3 = dp[row+1][col+1]
                #print(ans1,ans2,ans3)
                ans = arr[row][col]+ min(ans1,ans2,ans3)
                dp[row][col] = ans
                #print(ans)
    return dp[0][0]
            
            
costArr = [[5,1,19],[2,12,6],[7,4,9]]
print(minCostIter(costArr, 3, 3))
            
            
            
            
            
            
            
            
            
            
            
            
    
=======
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:44:44 2020

@author: cheerag.verma
"""
############################################### RECURSIVE PROGRAMMING ################################
import sys
def costFunction(costArr,m,n,i,j):
    
    #base case
    if i>=m or j>=n:
        return sys.maxsize
    #special case
    if i == m-1 and j == n-1:
        return costArr[i][j]
    
    ans1 = costFunction(costArr, m, n, i+1, j)
    ans2 = costFunction(costArr, m, n, i, j+1)
    ans3 = costFunction(costArr, m, n, i+1, j+1)
    
    result = costArr[i][j] + min(ans1,ans2,ans3)
    return result

    
m = 3
n = 3
#costArr = [[int(j) for j in input().split()] for i in range(m)]
costArr = [[5,1,19],[2,12,6],[7,4,9]]
print(costFunction(costArr,m,n,0,0))

############################################### RECURSIVE DYNAMIC PROGRAMMING ################################
import sys
def costFunction(costArr,m,n,i,j,dp):
    
    #base case
    if i>= m or j>= n:
        return sys.maxsize
    
    #special case to handle last grid
    if i == n-1 and j == m-1: 
        return costArr[i][j]
    
    # if i == n-1 or j == n-1:
    #     return sys.maxsize
    
    if dp[i+1][j] == sys.maxsize:
          ans1 = costFunction(costArr, m, n, i+1, j, dp)
          dp[i+1][j] = ans1
    else:
        ans1 = dp[i+1][j]

    if dp[i][j+1] == sys.maxsize:
        ans2 = costFunction(costArr, m, n, i, j+1, dp)
        dp[i][j+1] = ans2
    else:
        ans2 = dp[i][j+1]

    if dp[i+1][j+1] == sys.maxsize:
        ans3 = costFunction(costArr, m, n, i+1, j+1, dp)
        dp[i+1][j+1] = ans3
    else:
        ans3 = dp[i+1][j+1]
    
    print(ans1,ans2,ans3)
    result = costArr[i][j] + min(ans1,ans2,ans3)
    return result

    
#m = int(input())
m = 2
#n = int(input())
n = 2
costArr = [[5,1],[6,8]]
dp = [[sys.maxsize for j in range(n+1)]for i in range(m+1)]
print(costFunction(costArr,m,n,0,0,dp))

#m,n = [int(input) for input in input().split()]

import sys
def minCostIter(arr,m,n):
    ans1 = sys.maxsize
    ans2= sys.maxsize
    ans3 = sys.maxsize
    dp = [[sys.maxsize for j in range(m+1)]for i in range(n+1)]
    for row in range(m-1,-1,-1):
        for col in range(n-1,-1,-1):
            if row == m-1 and col == n-1:
                dp[row][col] = arr[row][col]
            else:
                ans1 = dp[row+1][col]
                ans2 = dp[row][col+1]
                ans3 = dp[row+1][col+1]
                #print(ans1,ans2,ans3)
                ans = arr[row][col]+ min(ans1,ans2,ans3)
                dp[row][col] = ans
                #print(ans)
    return dp[0][0]
            
            
costArr = [[5,1,19],[2,12,6],[7,4,9]]
print(minCostIter(costArr, 3, 3))
            
            
            
            
            
            
            
            
            
            
            
            
    
>>>>>>> e9f61ce6d8dd9e8eeb45fc231f5eaebe06d511c8
    