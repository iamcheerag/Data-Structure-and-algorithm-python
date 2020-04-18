# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:16:27 2020

@author: cheerag.verma
"""


class Stack:
    def __init__(self):
        self.__inputArray = []              #initialzation of input array 
        
    def push(self,data):
        return self.__inputArray.append(data)      #Inserting values inside list
  
    def pop(self):
        if self.isEmpty():                  #checking the instance of class if it's empty of not! 
            print("Stack is empty , nothing to pop")
            return 
        return self.__inputArray.pop()
        
    def size(self):
        lenOfArray = len(self.__inputArray)
        return lenOfArray
        
    def isEmpty(self):
        return self.size() == 0
             
        
    def top(self):
        if self.isEmpty():
            print("No top exist")
            return
        topElementIndex = len(self.__inputArray)-1
        return self.__inputArray[topElementIndex]
        
        