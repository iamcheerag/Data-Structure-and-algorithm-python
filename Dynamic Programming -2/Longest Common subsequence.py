# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:33:38 2020

@author: cheerag.verma
"""


# ================================= RECURSIVE SOLUTION ========================
def LCS(str1,str2,i,j):
    if str1 == None or str2 == None:
        return
    
    if i == len(str1) or j == len(str2):
        return 0
    
    
    if str1[i] == str2[j]:
        ans = 1+ LCS(str1,str2,i+1,j+1)
        return ans
    
    else :
        ans2 = LCS(str1,str2,i,j+1)
        ans3 = LCS(str1,str2,i+1,j)
        ans = max(ans2,ans3)
    return ans
    
    
str1 = 'cheerag'
str2 = 'verma'
print(LCS(str1,str2,i=0,j=0))

# =============================================================================

# =================================== DP RECURSIVE ============================
def LCSRecursive(str1,str2,i,j,dp):
    
    
    if i == len(str1) or j == len(str2):
        return 0
    
    if str1[i] == str2[j]:
        if dp[i+1][j+1] == -1:
            smallAns = LCSRecursive(str1,str2,i+1,j+1,dp)
            dp[i+1][j+1] = smallAns
            ans = 1 + smallAns
            
        else:
            ans = 1 + dp[i+1][j+1]
    
    
    else:
        if dp[i][j+1] == -1:
            ans1 = LCSRecursive(str1,str2,i,j+1,dp)
            dp[i][j+1]= ans1
        else:
            ans1 = dp[i][j+1]
        
        #print(ans1)
        if dp[i+1][j] == -1:
            ans2 = LCSRecursive(str1,str2,i+1,j,dp)
            dp[i+1][j] = ans2
        else:
            ans2 = dp[i+1][j]
            
        #print(ans2)
        ans = max(ans1,ans2)
    return ans
        
        
s1 ='abcd'
s2 ='bde'

dp = [[-1 for i in range(len(s2)+1)] for i in range(len(s1)+1)]
print(LCSRecursive(s1,s2,0,0,dp))
        
        
# =============================================================================
# ============================== DP Iterative =================================
   
def LCSIterative(str1,str2):
    dp = [[0 for j in range(len(str2)+1)]for i in range(len(str1)+1)]
    
    #bottom up approach
    for i in range(len(str1)-1,-1,-1):
        
        for j in range(len(str2)-1,-1,-1):
            if str1[i] == str2[j]:
                ans = 1 + dp[i+1][j+1]
            else:
                ans = max(dp[i][j+1], dp[i+1][j])
             
            dp[i][j] = ans
        
    return dp[0][0]
                
                    
str1 = 'cheerag'  
str2 = 'verma'
print(LCSIterative(str1, str2))
        
    
    
        
        
        




