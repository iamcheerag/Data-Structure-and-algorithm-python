# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:28:44 2020

@author: cheerag.verma
"""

#max heap inbuilts function

import heapq
li = [10,5,4,3,22,9,31]

heapq._heapify_max(li)  # builds the max heap 

heapq._heappop_max(li)  # pops the max element from the list

heapq._heapreplace_max(li,0)  # pops out the top element and replace it with 0 (element) and perform downheapify

# insert element in the max heap

li.append(20)
heapq._siftdown_max(li,0,len(li)-1)  #li,startposition,endposition

heapq._heapreplace_max(li)