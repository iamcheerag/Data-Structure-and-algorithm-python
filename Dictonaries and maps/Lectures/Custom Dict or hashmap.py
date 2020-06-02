# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:25:31 2020

@author: CHEERAG
"""


class MapNode:      #Linked List in open hashing technique
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        
        

class Map:
    def __init__(self):
        self.bucketSize= 10
        self.bucket = [None for i in range(self.bucketSize)]
        self.count = 0
        
    
    def size(self):
        return self.count
    
    def insert(self,key,value):
        hashCode = hash(key)
        index = abs(hashCode) % self.bucketSize
        head = self.bucket[index]
        
        while head is not None:
            if head.key == key:
                head.value = value
                return 
            head = head.next
        
        head = self.bucket[index]   # new node will be inserted from the front, so after coming out of the while loop this should point again back to bucket[index]
        newNode = MapNode(key,value)
        newNode.next = head
        self.bucket[index] = newNode
        self.count+=1
        
        
    def search(self,key):
        hashCode = hash(key)
        index = abs(hashCode) % self.bucketSize
        head = self.bucket[index]
        
        while head is not None:
            if head.key == key:
                return head.value
            
            head = head.next
        
        return None
       
        
    def remove(self,key):
        hashCode = hash(key)
        index = abs(hashCode) % self.bucketSize
        head = self.bucket[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.bucket[index] = head.next
                else:
                    prev.next = head.next
                
                self.count-=1
                return head.value
            prev = head
            head = head.next
            
            
        return None
        
m = Map()
m.insert('a',20)
print(m.size())
m.insert('b',20)
print(m.size())
m.insert('c',200)
print(m.size())
print(m.search('b'))
m.remove('a')
print(m.size())
        
        
