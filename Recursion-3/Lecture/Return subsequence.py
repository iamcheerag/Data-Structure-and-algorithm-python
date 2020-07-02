# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:26:59 2020

@author: cheerag.verma
"""


"""
Return Subsequences

Given a string (lets say of length n), return all the subsequences of the given string.
Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain same as in the input string.
Note : The order of subsequences are not important.
    Sample Input:
    abc
    Sample Output:
    "" (the double quotes just signifies an empty string, don't worry about the quotes)
    c 
    b 
    bc 
    a 
    ac 
    ab 
    abc 
"""





def subsequences(string):
    if len(string) ==0:
        arr =[]
        arr.append(" ")
        return arr
    
    smallOutput = subsequences(string[1:])
    for data in range(len(smallOutput)):
        smallOutput.append(string[0]+smallOutput[data])
    
    return smallOutput

string = "abc"
ans = subsequences(string)
for ele in ans:
    print(ele)
    
    
def subsequences_easy(string):
    if len(string) ==0:
        arr = []
        arr.append(" ")
        return arr
    
    smallOutput = subsequences_easy(string[1:])
    
    output = []

    #copying everything in the new array(output[])
    for data in smallOutput:
        output.append(data)
    
    for data in smallOutput:
        output.append(string[0]+data)
    
    return output

print(subsequences_easy("abc"))







    