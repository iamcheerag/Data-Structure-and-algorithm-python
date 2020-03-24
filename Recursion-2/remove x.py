# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:28:39 2020

@author: cheerag.verma
"""

'''
Given a string, compute recursively a new string where all 'x' chars have been removed.
Sample Input 1 : xaxb

Sample Output 1: ab
'''


def removeX(string):
    if len(string) == 0:
        return string

    smallList = string[1:]
    smallOutput = removeX(smallList)
    
    if string[0] == 'x':                   #smallOutput se string varible return hokar aya hai 
        return smallOutput
    else:
        return string[0] + smallOutput
    
str = input()
removeX(str)



def removeX(s):
    if len(s) == 0:
        return s 
    if s[0] == 'x':
        smallOutput = removeX(s[1:])
        print(smallOutput)
        return smallOutput
    else:
        smallOutput = removeX(s[1:])
        return s[0] + smallOutput
    
s= 'xxxxxxxxxxffdcc'
removeX(s)