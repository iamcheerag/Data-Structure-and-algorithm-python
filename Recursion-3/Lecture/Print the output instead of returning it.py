# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 07:11:44 2020

@author: cheerag.verma
"""

#=============================================================================
#This method will print all the factorial number , but we want only the ans
def fact(n):
    if n == 0:
        return 1
    
    smallOutput = n * fact(n-1)
    print(smallOutput)
    return smallOutput

print(fact(5))
#=============================================================================

#=============================================================================
# Simple yet not very satisfying method

def factHelper(n):
    if n == 0:
        return 1
    
    smallOutput = n * factHelper(n-1)
    return smallOutput


def fact(n):
    output = factHelper(n)
    print(output)

fact(5)
#=============================================================================

#rather than printing from bottom to top and terminating through base case
# will print from top to bottom and get print the ans in base condition

def printFact(n,ans):
    if n == 0:
        print(ans)
        return
        
    ans = ans * n               
    printFact(n-1, ans)



printFact(5, 1)














