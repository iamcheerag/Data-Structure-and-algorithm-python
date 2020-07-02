# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:45:21 2020

@author: cheerag.verma
"""

"""
0 1 Knapsack - Problem

A thief robbing a store and can carry a maximal weight of W into his knapsack. There are N items and ith item weigh wi and is value vi. What is the maximum value V, that thief can take ?
    Input Format :
        Line 1 : N i.e. number of items
        Line 2 : N Integers i.e. weights of items separated by space
        Line 3 : N Integers i.e. values of items separated by space
        Line 4 : Integer W i.e. maximum weight thief can carry
    Output Format :
        Line 1 : Maximum value V
    Constraints
        1 <= N <= 20
        1<= wi <= 100
        1 <= vi <= 100
    Sample Input 1 :
        4
        1 2 4 5
        5 4 8 6
        5
    Sample Output :
        13
"""
def knapsackRecursive(valArray,wArray,maxWeight,eleValue,i):
    if eleValue == i:
        return 0
        
    if wArray[i] > maxWeight:
        ans = knapsackRecursive(valArray, wArray, maxWeight, eleValue, i+1)
    
    else:
        #include the ith weight , hence decreasing the overall weight by subtracting the current ith weight
        ans1 = valArray[i] + knapsackRecursive(valArray,wArray, maxWeight-wArray[i], eleValue, i+1)
        
        #excluding the ith element 
        ans2 = knapsackRecursive(valArray, wArray, maxWeight, eleValue, i+1)
        ans = max(ans1,ans2)
        
    return ans

    
n = 4
valArray = [5,4,8,6]
wArray   = [1,2,4,5]
maxWeight = 5
eleValue = len(valArray)
print(knapsackRecursive(valArray, wArray, maxWeight, eleValue, i=0))
    
    
    
    
    

def knapsackRecursiveDP(valArray,wArray,maxWeight,eleValue,i,dp):
    if eleValue == i:
        return 0

    
    #when weight of the current val is more than maximum weight
    if wArray[i] > maxWeight:
        if dp[maxWeight][i+1] == -1:
            ans = knapsackRecursiveDP(valArray, wArray, maxWeight, eleValue, i+1,dp)
            dp[maxWeight][i+1] = ans
            
        else:
            ans = dp[maxWeight][i+1]
    
    else:
        #include the ith weight , hence decreasing the overall weight by subtracting the current ith weight
        if dp[maxWeight-wArray[i]][i+1] == -1:
            smallAns = knapsackRecursiveDP(valArray,wArray, maxWeight-wArray[i], eleValue, i+1,dp)
            dp[maxWeight-wArray[i]][i+1] = smallAns
            ans1 = valArray[i] + smallAns
        else:
            ans1 = valArray[i] + dp[maxWeight-wArray[i]][i+1]
        #excluding the ith element 
        if dp[maxWeight][i+1] == -1:
            ans2 = knapsackRecursiveDP(valArray, wArray, maxWeight, eleValue,i+1,dp)
            dp[maxWeight][i+1] = ans2
        else:
            ans2 = dp[maxWeight][i+1]
        

        ans = max(ans1,ans2)
        
    return ans

    
n = 4
valArray = [5,4,8,6]
wArray   = [1,2,4,5]
maxWeight = 5
eleValue = len(valArray)
dp = [[-1 for j in range(maxWeight+1)] for i in range(eleValue+1)]
i = 0
print(knapsackRecursiveDP(valArray, wArray, maxWeight, eleValue,i,dp))
    
    
    
    
    
    
    
    
    
    
    
    
    
    