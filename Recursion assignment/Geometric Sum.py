"""
Problem :   Given k, find the geometric sum i.e. 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
            using recursion. Return the answer.

Sample Input  : 3

Sample Output : 1.875

"""



def GpSum(n):
    if n == 0 :
        return 1
    
    smallList = GpSum(n-1)  # induction hypothesis
    return 2 ** n + smallList

n = int(input())
result = GpSum(n)
print("%.5f"%result)





