class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_element(self,data):
        
        NodeInstance = Node(data)
        if self.head is None:
            self.head = NodeInstance
            self.tail = NodeInstance
        
        else:
            self.tail.next = NodeInstance
            NodeInstance.prev = self.tail
            self.tail      = NodeInstance
            
    def delete_element(self,index):
        ptr = self.head
        lenptr = self.head
        i = 1
        count = 0
        while lenptr:
            lenptr = lenptr.next
            count+=1
        #print(count)
        
        if index >=2 and count >= index:                   
            while i < index -1:
                ptr = ptr.next
                i+=1
                
            if ptr.next.next is None:           #delete the last node
                ptr.next = None
                self.tail.prev = None
                self.tail = ptr
                
                
                return True
            else:                               #delete any node
                ptr.next = ptr.next.next
                ptr.next.prev = ptr
                return True
        
        elif index < 2:                         #delete the first node 
            self.head = ptr.next
            ptr.next = None
            self.head.prev = None
            return True
        
        
        else:
            return False
    
        
    def print_dll(self):
        ptr =self.head
        while ptr:
            print(ptr.data , end = " ")
            ptr = ptr.next
    
    def print_reverse_dll(self):
        ptr = self.tail
        #print()
        while ptr:
            print(ptr.data, end = " ")
            ptr = ptr.prev
    
    
        
        
if __name__ == "__main__":
    dll = doubly_linked_list()
    for data in list(range(2,7)):
        dll.insert_element(data)
        
    print("Original Linked List")
    dll.print_dll()
    print()
    print("========================")
    print("ENTER THE ELEMENT'S INDEX FOR DELETION")
    index = int(input())
    result = dll.delete_element(index)
    if result:
        print("linked list after deleting the Node:")
        dll.print_dll()
        print()
        print("reversed list:")
        dll.print_reverse_dll()
    else:
        print("Index out of range")
    
    
    

