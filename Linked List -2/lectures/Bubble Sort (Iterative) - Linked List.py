class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubbleSortLL(head) :
    #  Sort a given linked list using Bubble Sort (iteratively). While sorting,
    #  you need to swap the entire nodes, not just the data.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if head==None or head.next==None:
        return head
    swap=True
    while swap:
        swap=False
        prev=None
        curr=head
        next=curr.next
        while next:
            if curr.data>next.data:
                swap=True
                if prev:
                    prev.next=next
                else:
                    head=next
                curr.next=next.next
                next.next=curr
                prev=next
            else:
                prev=curr
            curr=prev.next
            next=curr.next
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
l = bubbleSortLL(l)
printll(l)
