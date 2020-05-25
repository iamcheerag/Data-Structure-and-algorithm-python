"""
Maximum Frequency

You are given an array of integers that contain numbers in random order. Write a program to find and return the number which occurs the maximum times in the given input.
If two or more elements contend for the maximum frequency, return the element which occurs in the array first.
	Input Format :
	Line 1 : An Integer N i.e. size of array
	Line 2 : N integers which are elements of the array, separated by spaces
	Output Format :
	Most frequent element
	Constraints :
	0 <= N <= 10^8
	
	Sample Input 1 :
	13
	2 12 2 11 12 2 1 2 2 11 12 2 6 
	Sample Output 1 :
	2
	
	Sample Input 2 :
	3
	1 4 5
	Sample Output 2 :
	1
"""


def maxFreq(l):
    d = {}
    for num in l:
        if num in d:
            d[num]+=1
        else:
            d[num] = 1
	
    tempValue = 0
    tempKey = l[0]
    
    for w in l:
        if d[w] > tempValue:
            tempValue = d[w]
            tempKey   = w
            
    print(tempKey)
    

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
maxFreq(l)
