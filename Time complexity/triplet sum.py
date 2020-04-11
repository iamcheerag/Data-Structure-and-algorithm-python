# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:07:33 2020

@author: cheerag.verma
"""

def tripletSum(a,sum_):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for k in range(j+1,len(a)):
                if i!=j!=k and a[i] + a[j] + a[k] == sum_:
                 
                    if a[i] > a[j] and a[i] > a[k] and a[j]>a[k]:
                        print(a[k],a[j],a[i])
                    
                    elif a[i] > a[j] and a[i] > a[k] and a[j]<a[k]:
                        print(a[j],a[k],a[i])
                    
                    elif a[j]>a[i] and a[j]>a[k] and a[k]>a[i] :
                        print(a[i],a[k],a[j])
                        
                    elif a[j]>a[i] and a[j]>a[k] and a[k]<a[i] :
                        print(a[k],a[i],a[j])
                    
                    elif a[k]>a[i] and a[k]>a[j] and a[i]>a[j]:
                        print(a[j],a[i],a[k])
                    
                    elif a[k]>a[i] and a[k]>a[j] and a[i]<a[j]:
                        print(a[i],a[j],a[k])
                        


tripletSum([1,2,3,4,5,6],7)