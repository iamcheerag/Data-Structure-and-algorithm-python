# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:38:12 2020

@author: cheerag.verma

Check redundant brackets

Given a string mathematical expression, return true if redundant brackets are present in the expression. Brackets are redundant if there is nothing inside the bracket or more than one pair of brackets are present.
Assume the given string expression is balanced and contains only one type of bracket i.e. ().
Note: You will not get partial score for this problem. You will get marks only if all test cases are passed.
Input Format :
String s (Expression)
Output Format :
true or false
Sample Input 1:
((a + b)) 
Sample Output 1:
true
Sample Input 2:
(a+b) 
Sample Output 2:
false
"""

def checkRedundant(inputString):
    flag = None
    stack = []
    for s in inputString:
        if s!=")":
            stack.append(s)
            #flag = False
        
        elif s == ")":
            flag = True
            while stack[len(stack)-1]!="(":   #top
                stack.pop()
                flag = False
            stack.pop()
            if flag == True:
                return True
            
    return flag
#### Implement Your Code Here
    

string = "(+())"
ans = checkRedundant(string)
print(ans)
# if ans is True:
#     print('true')
# else:
#     print('false')

