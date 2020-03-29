# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:29:45 2020

@author: cheerag.verma
"""

"""
Given a string, compute recursively a new string where all 'x' chars have been removed.
Sample Input 1 : xaxb

Sample Output 1: ab
"""




def removeX(str):
    if len(str) == 0:
        return str

    smallList = str[1:]
    smallOutput = removeX(smallList)
    
    if str[0] == 'x':
        return smallOutput
    else:
        return str[0] + smallOutput

# Main
string = input()
print(removeX(string))
