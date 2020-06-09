# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:25:41 2020

@author: cheerag.verma

Longest subset zero sum

Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.
NOTE: You have to return the length of longest subarray .
	Input Format :
	Line 1 : Contains an integer N i.e. size of array

	Line 2 : Contains N elements of the array, separated by spaces
	Output Format
	 Line 1 : Length of longest subarray 
	Constraints:
	0 <= N <= 10^8
	
	Sample Input :
	10 
	 95 -97 -387 -435 -5 -70 897 127 23 284
	Sample Output :
	5
"""
 
def subsetSum(arr):
    dataDict = {}
    digitSum = 0
    maxLen = 0
    
    if len(arr) == 1 and arr[0]==0:
        return 1
    
    for idx in range(len(arr)):
        digitSum = digitSum + arr[idx]

        if digitSum in dataDict:
            start = dataDict[digitSum] 
            end = idx
            tempLen = end-start

            if tempLen > maxLen:
                maxLen = tempLen
        
        else:
            dataDict[digitSum] = idx 

        if digitSum == 0 and arr[0]!=0:
            tempLen = len(dataDict)
            if tempLen > maxLen:
                maxLen = tempLen+1

    return maxLen  


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
finalLen= subsetSum(l)
print(finalLen)