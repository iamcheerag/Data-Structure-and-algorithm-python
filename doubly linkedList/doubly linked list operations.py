class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self,data):
        NodeInstance = Node(data)
        
        if self.head is None:
            self.head = NodeInstance
            self.tail = NodeInstance
            
        else:
            self.tail.next      = NodeInstance
            NodeInstance.prev   = self.tail
            NodeInstance.next   = None
            self.tail           = NodeInstance
            
    def insertAtbeginning(self,data):
        NodeInstance = Node(data)
        
        if self.head is None:
            self.head = NodeInstance
            self.tail = NodeInstance
        else:
            NodeInstance.next = self.head
            NodeInstance.prev = None
            self.head.prev    = NodeInstance
            self.head         = NodeInstance
        
        
    def insertAtEnd(self,data):
        NodeInstance = Node(data)
        
        if self.head is None:  #if no element in the linkedlist
          NodeInstance.prev = None
          self.head = NodeInstance
        
        else:
            self.tail.next = NodeInstance
            NodeInstance.next = None
            NodeInstance.prev = self.tail
            self.tail = NodeInstance
    
    
    
    def insertAfterGivenNode(self,index,data):
        try:
            NodeInstance = Node(data)
            ptr = self.head
            lenptr = self.head
            i=1
            count=1
            while lenptr:
                lenptr= lenptr.next
                count +=1
            
            if index > count:
                print("Error : Enter the correct index")
                return False
        
            while i <= index - 1:
                ptr = ptr.next
                i+=1
                
            if self.tail is None:
                NodeInstance.prev = self.tail
                NodeInstance.next = None
                self.tail = NodeInstance
            
            else:
                NodeInstance.next = ptr.next
                ptr.next.prev     = NodeInstance
                ptr.next          = NodeInstance
                NodeInstance.prev = ptr
                
        except:
            pass
    
    def insertBeforeGivenNode(self,index,data):
        NodeInstance = Node(data)
        
        ptr = self.head
        i=1
        while i < index:
            ptr = ptr.next
            i+=1

        NodeInstance.next = ptr
        ptr.prev.next     = NodeInstance
        NodeInstance.prev = ptr.prev
        ptr.prev          = NodeInstance
        
        
            
    def display(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data , end = " ")
            ptr = ptr.next
        
        
        
    def reverseDisplay(self):
        print()
        ptr = self.tail
        while ptr is not None:
            print(ptr.data, end = " ")
            ptr = ptr.prev
        

if __name__ == "__main__":
    dll = doubly_linked_list()
    for data in list(range(3,8)):
        dll.insert(data)
    
    print("INSERTION AT THE BEGINNING")
    print("ENTER THE NUMBER TO BE INSERTED AT THE BEGINING")
    number = int(input())
    dll.insertAtbeginning(number)
    dll.display()
    dll.reverseDisplay()
    print("\n-------------------------------------")
    
    print("INSERTION AT THE  END")
    print("ENTER THE NUMBER TO BE INSERTED AT THE END")
    number2 = int(input())
    dll.insertAtEnd(number2)
    dll.display()
    dll.reverseDisplay()
    print("\n-------------------------------------")
   
    print("INSERTION AFTER THE  GIVEN NODE")
    print("ENTER THE INDEX AND NUMBER")
    index = int(input())
    number3 =int(input())
    returnResult = dll.insertAfterGivenNode(index,number3)
    if returnResult:
        dll.display()
        dll.reverseDisplay()
    print("\n-------------------------------------")
    
    print("INSERTION BEFORE THE  GIVEN NODE")
    print("ENTER THE INDEX AND NUMBER")
    index2 = int(input())
    number4 =int(input())
    dll.insertBeforeGivenNode(index2,number4)
    returnResult1 = dll.insertAfterGivenNode(index,number3)
    if returnResult1:
        dll.display()
        dll.reverseDisplay()
    
    print("\n-------------------------------------")
