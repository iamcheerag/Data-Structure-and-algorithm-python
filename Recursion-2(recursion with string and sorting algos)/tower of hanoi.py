# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 13:13:44 2020

@author: cheerag.verma
"""

def towerOfHanoi(n,source,auxi,destination):
    if n == 1:
        print("move 1st disk",source," to ",destination)
        return
        
    towerOfHanoi(n-1,source,destination,auxi)  #n-1 disk moved  induction step n-1 disk ko utahakar rkh do b peh kaise ho yeh recursion dekhega apun nhi 
    print("move",n,"th disk from",source," to ",destination)
    towerOfHanoi(n-1,auxi,source,destination)
    
    
n = 3
towerOfHanoi(n, 'a', 'b', 'c')    
