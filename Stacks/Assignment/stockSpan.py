# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:39:23 2020

@author: cheerag.verma
"""


def stockSpan(price,n):
    stack = []
    result = []
    result.append(1)
    stack.append(0)
    
    for i in range(1,len(price)):
        flag = False
        while price[stack[-1]] < price[i] :
            stack.pop()
            flag = True
            if len(stack) == 0:
                result.append(i+1)
                stack.append(i)
                break
        else:
            if price[stack[-1]] > price[i] :
                result.append(i-stack[-1])
                stack.append(i)
            
            elif flag == True:
                result.append(i-stack[-1])
            
            elif price[stack[-1]] == price[i]:
                result.append(1)
                stack.append(i)
                


    return result

# n = int(input())
# price = [int(ele) for ele in input().split()]
price = [1,2,2,1,2,3]
n = 6
spans = stockSpan(price,n)
for ele in spans:
    print(ele,end= ' ')
