# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:13:16 2020

@author: cheerag.verma
"""

"""
Pair sum in array

Given a random integer array A and a number x. Find and print the pair of elements in the array which sum to x.
Array A can contain duplicate elements.
While printing a pair, print the smaller element first.
That is, if a valid pair is (6, 5) print "5 6". There is no constraint that out of 5 pairs which have to be printed in 1st line. You can print pairs in any order, just be careful about the order of elements in a pair.

Input format :
Line 1 : Integer N (Array size)
Line 2 : Array elements (separated by space)
Line 3 : Integer x

Output format :
Line 1 : Pair 1 elements (separated by space)
Line 2 : Pair 2 elements (separated by space)
Line 3 : and so on

Constraints :
1 <= N <= 1000
1 <= x <= 100

Sample Input:
9
1 3 6 2 5 4 3 2 4
7

Sample Output :
1 6
3 4
3 4
2 5
2 5
3 4
3 4
"""

def pairSum(arr,x):
    arr.sort() # nlogn
    i = 0 
    j = len(arr)-1
    
    while i < j:
        if arr[i] + arr[j] > x:
            j-=1
        
        elif arr[i] + arr[j] < x:
            i+=1
            
        else:
            
            print(arr[i], arr[j])

            if arr[j - 1] == arr[j] and arr[i + 1] == arr[i]:
                print(arr[i], arr[j])
                print(arr[i], arr[j])
                i+=1
                j-=1
                

            elif arr[j-1] == arr[j]:
                j-=1
            
            elif arr[i+1] == arr[i]:
                i+=1
            
            else:
                i+=1
                j-=1
            
arr = [1,3,6,2,5,4,3,2,4]
x = 7
pairSum(arr,x)






arr = [1,3,6,2,5,4,3,2,4]
freq_dict = {}
count = 1
x = 7
for data in arr:
    if data in freq_dict:
        freq_dict[data] = freq_dict[data]+1
    else:
        freq_dict[data] = count


for i in range(len(arr)):
    counterPart = x-arr[i]
    if counterPart in freq_dict:
        printTimes = freq_dict[counterPart] * freq_dict[arr[i]]
        #print(printTimes,freq_dict[counterPart] , freq_dict[arr[i]])
        if arr[i]<counterPart:
            print(arr[i],counterPart)*printTimes
        else:
            print(counterPart,arr[i]) * printTimes
    
        freq_dict[counterPart] = 0
        freq_dict[arr[i]] = 0
    











arr = [2,2,2,2]
freq_dict = {}
count = 1
x = 5
for data in arr:
    if data in freq_dict:
        freq_dict[data] = freq_dict[data]+1
    else:
        freq_dict[data] = count

#print(freq_dict)

for i in range(len(arr)):
    counterPart = x-arr[i]
    if counterPart in freq_dict and freq_dict.get(counterPart)!=0 and freq_dict.get(arr[i])!=0:
        m=freq_dict.get(counterPart)
        n=freq_dict.get(arr[i])
        
        if arr[i]!=counterPart:
            for j in range(n*m):
                print(arr[i],counterPart)
            freq_dict[counterPart]=0
            freq_dict[arr[i]]=0
        else :
            for j in range(n//2):
                print(arr[i],counterPart)
            freq_dict[counterPart]=0
            freq_dict[arr[i]]=0












