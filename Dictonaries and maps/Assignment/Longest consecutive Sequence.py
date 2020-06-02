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
    
    
#inputArr =[2,12,9,16,10,5,3,20,25,11,1,8,6]
#inputArr = [7,8,9,6,5,12,1,2]
#inputArr = [-2,-3,-1,-5,10,6,7,8]
#inputArr = [9,3,2,7,8,10,5,4]
#inputArr = [3,7,2,1,9,8]


#startIndex = 0



def longestConsecutiveSq(inputArr):
    freqDict = {}
    freqDict = freqDict.fromkeys(inputArr, True)
    length = 0
    startIndex = 0
    for element in inputArr:
        tempLength = 0
        tempStart = 0
        if freqDict[element] == True:
            freqDict[element] = False
            tempLength +=1
            tempStart = element
            
            #moving forward
            forwardElement = element+1
            while forwardElement in freqDict:
                freqDict[forwardElement] = False
                tempLength+=1
                forwardElement+=1
                
            
            #moving backward
            backwardElement = element-1
            while backwardElement in freqDict:
                freqDict[backwardElement] = False
                tempLength+=1
                tempStart = backwardElement
                backwardElement-=1
            
            if tempLength > length:
                length = tempLength
                startIndex = tempStart
            
            
            elif tempLength == length:
                tempStartIndexInActualArray = inputArr.index(tempStart)
                startIndexInActualArray = inputArr.index(startIndex)
                startIndex = inputArr[min(tempStartIndexInActualArray,startIndexInActualArray)]
                
    
    
    for data in range(startIndex,startIndex+length):
        print(data)



inputArr = [int(x) for x in input().split(" ")]
longestConsecutiveSq(inputArr)



















