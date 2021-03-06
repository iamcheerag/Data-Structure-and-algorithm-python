def downHeapify(arr,i,n):
    parentIndex = i
    minIndex = parentIndex
    leftChildIndex =  2 * parentIndex +1
    rightChildIndex = 2 * parentIndex + 2
    
    while leftChildIndex < n:
        
        if arr[minIndex] > arr[leftChildIndex]:
            minIndex = leftChildIndex
            
        if rightChildIndex < n and arr[minIndex] > arr[rightChildIndex]:
            minIndex = rightChildIndex
            
        if minIndex == parentIndex:
            return
        
        arr[minIndex], arr[parentIndex] =  arr[parentIndex], arr[minIndex]
        parentIndex = minIndex
        
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex= 2 * parentIndex + 2
        
    return 

def heapSort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        downHeapify(arr,i,n)
    
    for i in range(n-1,0,-1):
        arr[0], arr[i] = arr[i],arr[0]
        downHeapify(arr, 0, i)  
        
    return
        
 
arr = [2,6,8,5,4,3]
heapSort(arr)
for ele in arr:
    print(ele,end=" ")