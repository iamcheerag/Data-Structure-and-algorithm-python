# -*- coding: utf-8 -*-
"""
Created on Sun May 31 09:44:31 2020

@author: cheerag.verma
"""

class PriorityQueueNode:
    def __init__(self,element,priority):
        self.element  = element
        self.priority = priority

class maxPriorityQueue:
    def __init__(self):
        self.pq = []
    
    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def __percolateUp(self):  # or upHeapify
        childIndex  = self.getSize()-1
        parentIndex = (childIndex-1)//2
        
        while childIndex > 0:
            if self.pq[childIndex].priority > self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
                childIndex = parentIndex
                
            else:
                break
    
    def insert(self,element,priority):
        pqNode = PriorityQueueNode(element, priority)
        self.pq.append(pqNode)
        self.__percolateUp()
    
    def __procolateDown(self):
        parentIndex     = 0 
        leftChildIndex  = 2*parentIndex+1
        rightChildIndex = 2*parentIndex+2
        
        while leftChildIndex < self.getSize():
            minIndex = parentIndex
            
            if leftChildIndex< self.getSize() and self.pq[leftChildIndex].priority > self.pq[minIndex].priority:
                minIndex = leftChildIndex
                
            if rightChildIndex < self.getSize() and self.pq[rightChildIndex].priority > self.pq[minIndex].priority:
                minIndex = rightChildIndex
                
            if minIndex == parentIndex:
                break
            
            self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
            parentIndex     = minIndex
            leftChildIndex  = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2                
        
    
    def removeMax(self):
        if self.isEmpty():
            return None
        removedElement = self.pq[0].priority
        self.pq[0]     = self.pq[-1]
        self.pq.pop()
        self.__procolateDown()
        return removedElement
    
    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0].priority
    

maxPq = maxPriorityQueue()
maxPq.insert(3,3)
maxPq.insert(4,4)
maxPq.insert(63,63)
maxPq.insert(21,21)
maxPq.insert(9,9)
print(maxPq.getMax())
print(maxPq.removeMax())
maxPq.insert(7, 7)
print(maxPq.getMax())
print(maxPq.removeMax())
print(maxPq.getMax())

