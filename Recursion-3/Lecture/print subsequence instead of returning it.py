# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 07:53:45 2020

@author: cheerag.verma
"""


def printSubsq(string,output =""):
    if len(string) == 0:  #if input string is empty
        print(output)
        return 
    
    
    printSubsq(string[1:], output + string[0] )
    printSubsq(string[1:],output)
    
    
string = "abc"
printSubsq(string)

