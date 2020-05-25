# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:23:32 2020

@author: cheerag.verma


Longest consecutive Sequence

You are given with an array of integers that contain numbers in random order. Write a program to find the longest possible sequence of consecutive numbers using the numbers from given array.
You need to return the output array which contains consecutive elements. Order of elements in the output is not important.
Best solution takes O(n) time.
If two sequences are of equal length then return the sequence starting with the number whose occurrence is earlier in the array.
	Input Format :
	Line 1 : Integer n, Size of array
	Line 2 : Array elements (separated by space)
	Constraints :
	0 <= n <= 10^8
	Sample Input 1 :
	13
	2 12 9 16 10 5 3 20 25 11 1 8 6 
	Sample Output 1 :
	8 
	9 
	10 
	11 
	12

	Sample Input 2 :
	7
	3 7 2 1 9 8 1
	Sample Output 2 :
	7
	8
	9
	Explanation: Sequence should be of consecutive numbers. Here we have 2 sequences with same length i.e. [1, 2, 3] and [7, 8, 9], but output should be [7, 8, 9] because the starting point of [7, 8, 9] comes first in input array.
	
	Sample Input 3 :
	7
	15 24 23 12 19 11 16
	Sample Output 3 :
	15 
	16

"""
    
    
inputArr = [1,2,3,4,6,7,8,9]    
numDict = {}
numDict = numDict.fromkeys(inputArr, True)
startNum = 0

lenOfSq = 0

for element in inputArr:
    tempLenOfSq = 0
    
    if numDict[element] == True:
        numDict[element] = False
        tempLenOfSq+=1
        
        if startNum == 0:
            startNum = element
        elif startNum > element:
            startNum = element
        
        tempStart = element
        
        num = element+1
        while num in numDict and numDict[num] == True:
            numDict[num] = False
            tempLenOfSq+=1
            tempStart = num
            num+=1
        
        numBackward = element-1
        while numBackward in numDict and numDict[numBackward] == True:
            numDict[numBackward] = False
            tempStart = numBackward
            tempLenOfSq+=1
            numBackward-=1
            
        if tempLenOfSq > lenOfSq:
            lenOfSq = tempLenOfSq
            
            if tempStart < startNum:
                startNum = tempStart
            

        elif tempLenOfSq == lenOfSq:
            startNum = inputArr[min(inputArr.index(element),inputArr.index(startNum))]
            
        #print(startNum,lenOfSq)
        #startNum = element
    
print(startNum,lenOfSq)
for result in range(startNum,startNum+lenOfSq):
    print(result)
                
