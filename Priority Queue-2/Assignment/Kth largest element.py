# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:49:39 2020

@author: cheerag.verma
"""

import heapq

def kLargestElement(li,k):
    heapq._heapify_max(li)
    return li[k-1]        



li =[ int(x) for x in input().split()]
print(kLargestElement(li, 4))