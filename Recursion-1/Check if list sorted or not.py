# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:59:05 2020

@author: cheerag.verma
"""

def isSorted(l):
    list_ = len(l)
    if list_ == 0 or list_ == 1 :
        return True
    
    if l[0] > l[1]:
        return False
    
    smallerList = l[1:]
    smallerListOutput = isSorted(smallerList)
    if smallerListOutput:
        return True
    else:
        return False

l = [1,2,93,4,5]
isSorted(l)