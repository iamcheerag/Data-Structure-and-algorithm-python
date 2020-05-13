class GenericTreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

def takeInput():
    rootData = int(input("Enter Root:"))
    if rootData == -1:
        return None
    root = GenericTreeNode(rootData)
    print("Enter the number of child of ",rootData)
    childInput = int(input())

    for i in range(childInput):
        child = takeInput()
        root.children.append(child)
    return root

def printTree(root):
    if root == None:
        return None

    print(root.data,":",end = " ")
    for i in root.children:
        print(i.data,end = ",")
    print()

    for i in root.children:
        printTree(i)
    

def countNumberOfNodes(root):
    if root == None:  #edge case not a base case
        return 0
    count = 1
    for i in root.children:
        count= count + countNumberOfNodes(i)
    return count

root = takeInput()
printTree(root)
print("-------------------")
print(countNumberOfNodes(root))