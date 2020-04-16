"""
Delete every N nodes

Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same until end of the linked list. That is, in the given linked list you need to delete N nodes after every M nodes.
Input format :

Line 1 : Linked list elements (separated by space and terminated by -1)

Line 2 : M

Line 3 : N

    Sample Input 1 :
        1 2 3 4 5 6 7 8 -1
        2
        2
    Sample Output 1 :
        1 2 5 6
    
    Sample Input 2 :
        1 2 3 4 5 6 7 8 -1
        2
        3
    Sample Output 2 :
        1 2 6 7

"""





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N):
    if head is None:
        return None
    if m ==0 :
        return None
    
    current = head
    #newCurrent = None    
    while current is not None:
        for i in range(M-1):
            if current is None:
                return
            current = current.next
         
        if current is None:
            return 
        
        newCurrent= current.next
        
        for j in range(N):
            if newCurrent is None:
                break
            newCurrent = newCurrent.next
        
        
        current.next = newCurrent
        current = current.next
    
    return head
        
    
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
m=int(input())
n=int(input())
l = skipMdeleteN(l, m, n)
printll(l) 
