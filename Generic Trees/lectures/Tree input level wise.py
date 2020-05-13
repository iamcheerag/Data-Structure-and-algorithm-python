import queue
class GenericTree:
    def __init__(self,data):
        self.data = data
        self.children= []


def takeInputLevelWise():
    rootData = int(input('Enter root:'))
    if rootData == -1:
        return
    root = GenericTree(rootData) 
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        curr_element = q.get()
        print("No of children for", curr_element.data)
        childCount = int(input())
        for i in range(childCount):
            print("Enter the child")
            child = int(input())
            childRoot = GenericTree(child)
            curr_element.children.append(childRoot)
            q.put(childRoot)
        
    return root

def printTreeLevelWise(root):
    if root == None:
        return 
    q1 = queue.Queue()
    q1.put(root)

    while not q1.empty():
        curr = q1.get()
        print(curr.data,":",end="")
        for child in curr.children:
            print(child.data,end=",")
            








root = takeInputLevelWise()
printTreeLevelWise(root)


