# =============================================================================
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
#         
#         
#         
# class doublylinkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         
#     def insertEnd(self,data):
#         Nodeinstance = Node(data)
#         
#         if self.head is None:
#             self.head = Nodeinstance
#             self.tail = Nodeinstance
#         else:
#             self.tail.next      = Nodeinstance
#             Nodeinstance.prev   = self.tail
#             self.tail           = Nodeinstance
#             
#     def insertTail(self,data):
#         Nodeinstance = Node(data)
#         if self.head is None:
#             self.head = Nodeinstance
#             self.tail = Nodeinstance
#         else:
#             self.head.prev           = Nodeinstance
#             Nodeinstance.next        = self.head
#             self.head                = Nodeinstance
#         
#   
#     def print(self):
#         ptr = self.head
#         while ptr:
#             print(ptr.data, end = " , " )
#             ptr = ptr.next
#             
#     def revereseDisplay(self):
#         temp = self.tail
#         while temp :
#             print(temp.data, end = " , " )
#             temp = temp.prev
#             
# 
# if __name__=="__main__":
#     dll = doublylinkedlist()
#     
#     for data in list(range(0,6)):
#         dll.insert(data)
#     
#     dll.print()
#     print("\n")
#     dll.revereseDisplay()
#     


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def insert(self,root , data):
        if root is None:    
            self.head = Node(data)
            
        else:
            if root.next:
                self.insert(root.next , data)
            else:
                root.next = Node(data)
                
        
    def printRecursion(self):
        if self.head is None:
            return False
        else:
            print(self.head.data)
            self.head = self.head.next
            return self.printRecursion()

        

if __name__ =="__main__":
    ll = linkedList()
    for data in list(range(2,7)):
        ll.insert(ll.head , data)

    ll.printRecursion()






























