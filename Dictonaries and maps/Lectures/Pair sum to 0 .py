"""
Pair Sum To 0

Given a random integer array A of size N. Find and print the pair of elements in the array which sum to 0.
Array A can contain duplicate elements.
While printing a pair, print the smaller element first.
That is, if a valid pair is (6, -6) print "-6 6". There is no constraint that out of 5 pairs which have to be printed in 1st line. You can print pairs in any order, just be careful about the order of elements in a pair.
	Input format :
	Line 1 : Integer N (Array size)
	Line 2 : Array elements (separated by space)
	Output format :
	Line 1 : Pair 1 elements (separated by space)
	Line 2 : Pair 2 elements (separated by space)
	Line 3 : and so on
	Constraints :
	0 <= N <= 10^4
	
	Sample Input:
	5
	2 1 -2 2 3
	
	Sample Output :
	-2 2
	-2 2
"""


def pairSumToZero(a):
    numDict = {}
    for data in a:
        if data in numDict:
            numDict[data] = numDict[data]+1
        else:
            numDict[data]=1
            
            
    for key in a:
        if -key in numDict and numDict[-key]>0: 
            loopCount = numDict[key] * numDict[-key]
            for i in range(loopCount):
                if key < 0:
                    print(key,-key)
                else:
                    print(-key,key)
            
        numDict[key] = 0
        numDict[-key]=0
        
#Implement Your Code Here


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pairSumToZero(l)