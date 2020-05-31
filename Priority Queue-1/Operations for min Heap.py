# -*- coding: utf-8 -*-
"""
Created on Sat May 30 21:07:32 2020

@author: cheerag.verma
"""

class PriorityQueueNode:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []
        
    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self): # return True if size is 0
        return self.getSize == 0
        
    def __upHeapify(self, pqNode):
        childIndex  = self.getSize()-1
        
        while childIndex >0:
            parentIndex = (childIndex -1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                #swap
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
        
            else:
                break
        
        
        
    def insert(self, element, priority):
        pqNode = PriorityQueueNode(element, priority)
        self.pq.append(pqNode)
        self.__upHeapify(pqNode)
        
    def __percolateDown(self):
        parentIndex = 0
        
        
        leftChildIndex   = 2*parentIndex+1  
        rightChildIndex  = 2*parentIndex+2
        
        while leftChildIndex < self.getSize():
            minIndex = parentIndex
            
            if leftChildIndex < self.getSize() and self.pq[minIndex].priority > self.pq[leftChildIndex].priority:
                #self.pq[minIndex], self.pq[leftChildIndex] = self.pq[leftChildIndex], self.pq[minIndex]
                minIndex = leftChildIndex
                
            if rightChildIndex < self.getSize() and self.pq[minIndex].priority > self.pq[rightChildIndex].priority:
                #self.pq[minIndex], self.pq[rightChildIndex] = self.pq[rightChildIndex], self.pq[minIndex]
                minIndex = rightChildIndex
            
            if parentIndex == minIndex :
                break
            
            self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
            
            parentIndex = minIndex
            leftChildIndex  = 2*parentIndex+1
            rightChildIndex = 2*parentIndex+2
            
            
    
    def removeMin(self):
        if self.isEmpty():
            return None
        removedElement = self.pq[0].priority
        self.pq[0] = self.pq[-1]
        self.pq.pop()
        self.__percolateDown()
        
        return removedElement
        
    
pq = PriorityQueue()
pq.insert('A', 10)
pq.insert('B', 4)
pq.insert('C', 14)
pq.insert('D', 1)
pq.insert('E', 40)

pq.getSize()
pq.isEmpty()


for i in range(5):
    print(pq.removeMin())
        