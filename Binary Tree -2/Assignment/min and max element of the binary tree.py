"""
Min and max

Given a binary tree, find and return the min and max data value of given binary tree.
Return the output as an object of PairAns class, which is already created.
    Input format :
    Elements in level order form (separated by space)
    (If any node does not have left or right child, take -1 in its place)
    
    Output Format :
    Max and min (separated by space)
    
    Sample Input :
    8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
    
    Sample Output :
    14 1
"""


class BinaryTree:
    def __init__(self,data):
        self.data  = data
        self.left  = None
        self.right = None

import queue
def takeInputLevelOrder():
    q = queue.Queue()
    rootData = int(input("Enter root:"))
    if rootData == -1:
        return 
    
    root = BinaryTree(rootData)
    q.put(root)
    
    while not q.empty():
        current = q.get()
        
        leftCurrent = int(input("Enter left child:"))
        if leftCurrent!=-1:
            leftChild = BinaryTree(leftCurrent)
            current.left = leftChild
            q.put(leftChild)
         
        rightCurrent = int(input("Enter right child:"))               
        if rightCurrent!=-1:
            rightChild = BinaryTree(rightCurrent)
            current.right = rightChild
            q.put(rightChild)
            
    return root

def minMax(root,minData,maxData):
    if root is None:
        return

    minData,maxData = minMax(root.left)
    minData,maxData = minMax(root.right)
    
    if root.left is not None:
        leftData = root.left.data
        if leftData <= minData:
            global minData 
            minData = leftData
            
        
        elif leftData >= maxData:
            global maxData
            maxData = leftData
            
    if root.right is not None:
        rightData = root.right.data
        if rightData <= minData:
            global minData 
            minData = rightData
        
        elif rightData >=maxData:
            global maxData 
            maxData = rightData
        
    return minData,maxData

        
root = takeInputLevelOrder()
minData ,maxData = minMax(root)
print(maxData,minData)



