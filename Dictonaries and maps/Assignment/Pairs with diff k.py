# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:30:11 2020

@author: cheerag.verma


Pairs with difference K

You are given with an array of integers and an integer K. Write a program to find and print all pairs which have difference K.
Take difference as absolute.
	Input Format :
	Line 1 : Integer n, Size of array
	Line 2 : Array elements (separated by space)
	Line 3 : K
	Output format :
	Print pairs in different lines (pair elements separated by space). In a pair, smaller element should be printed first.
	(Order of different pairs is not important)
	Constraints :
	0 <= n <= 10^4
	
	Sample Input 1 :
	4 
	5 1 2 4
	3
	Sample Output 1 :
	2 5
	1 4
	
	Sample Input 2 :
	4
	4 4 4 4 
	0
	Sample Output 2 :
	4 4
	4 4
	4 4
	4 4
	4 4
	4 4
"""


arr =[]
k = 0
numDict = {}

for data in arr:
    if data in numDict:
        numDict[data]+=1
    else:
        numDict[data]=1
    
for num in arr:
    if k!=0:
        flag = False
        otherNum = num - k
        if otherNum < 0:
            flag = True
            otherNum = k + num
        
        if otherNum in numDict and numDict[otherNum]!=0:
            loopCount = numDict[num] * numDict[otherNum]
            for i in range(loopCount):
                if flag:
                    print(num,otherNum)
                else:
                    print(otherNum,num)
            
            numDict[num] = 0
            numDict[otherNum] = 0
    else:
        n = len(arr)
        count = (n-1)*(n)//2
        for i in range(count):
            print(num,num)
        break
        