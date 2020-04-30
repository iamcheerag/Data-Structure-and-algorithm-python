# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:07:33 2020

@author: cheerag.verma
"""

def tripletSum(a,sum_):
    for i in range(len(a)):
        for j in range(len(a),0,-1):
            ele= sum_-a[i]-a[j]
            
            if ele in a and i!=j!=ele :
                if a[i]>a[j] and a[i]>ele and a[j]>ele:  #i greater
                    print(ele,a[j],a[i])
                
                elif a[i]>a[j] and a[i]>ele and a[j]< ele:
                    print(a[j],ele,a[i])
                    
                
                elif a[j]>a[i] and a[i]>ele and a[i]>ele:
                    print(ele,a[i],a[j])
                
                elif a[j]>a[i] and a[i]>ele and a[i]<ele:
                    print(a[i],ele,a[j])
                    
                
                elif ele > a[i] and ele > a[j] and a[i]>a[j]:
                    print(a[j],a[j],ele)
                    
                elif ele > a[i] and ele > a[j] and a[i]<a[j]:
                    print(a[i],a[j],ele)
                    
            else:
                pass

newArray=[]
tripletSum([1,2,3,4,5,6,7],12)














def pairSum(li, x):
    li.sort()
    for i in range(len(li)-2):
        for j in range(len(li)-1,i+1,-1):
            f=x-(li[i]+li[j])
            s=i+1
            e=j-1
            m=(s+e)//2
            while s<=e:
                if li[m]==f:
                        d=m
                    while li[d]==f and d>=s:
                        print(li[i],li[m],li[j])
                        d-=1
                    d=m+1   
                    while li[d]==f and d<=e:
                        d+=1
                        print(li[i],li[m],li[j])
                    break
                elif li[m]>f:
                    e=m-1
                    m=(s+e)//2
                elif li[m]<f:
                    s=m+1
                    m=(s+e)//2