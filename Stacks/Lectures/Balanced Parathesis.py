"""

Balanced Paranthesis

Given a string expression, check if brackets present in the expression are balanced or not. Brackets are balanced if the bracket which opens last, closes first.
You need to return true if it is balanced, false otherwise.
Note: This problem was asked in initial rounds in Facebook
    Sample Input 1 :
    { a + [ b+ (c + d)] + (e + f) }
    Sample Output 1 :
    true
    Sample Input 2 :
    { a + [ b - c } ]
    Sample Output 2 :
    false

"""


def balancedParanthesis(str):    
    stack = []
    for ch in str:
        if ch in "[{(":
            stack.append(ch)
        
        elif ch == "}":
            if len(stack) == 0 or stack[-1]!= "{":
                return False
            else:
                stack.pop()
                

        elif ch == ")":
            if len(stack) == 0 or stack[-1]!= "(":
                return False
            else:
                stack.pop()
                
        elif ch == "]":
            if len(stack) == 0 or stack[-1]!= "[":
                return False
            else:
                stack.pop()
                
                
    if len(stack) == 0:
        return True
    else:
        return False
    
    
exp=input()
if balancedParanthesis(exp):
    print('true')
else:
    print('false')