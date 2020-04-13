class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
def createLL(arr):
    if len(arr)== 0:
        return 
    
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    
    return head

def reverseLL(head):
    current = head
    prev=None
    
    while current is not None:
        next_ = current.next 
        current.next = prev
        prev = current
        current = next_
    head = prev
    
    return head
    

def printLL(head):
    current = head
    while current is not None:
        print(current.data,end= " ")
        current = current.next
        
        
arr = [int(x) for x in input().split()]
head = createLL(arr[:-1])
head = reverseLL(head)
printLL(head)