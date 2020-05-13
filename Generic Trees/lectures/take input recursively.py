class GenericTreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

def takeTreeInput():
    rootData = int(input("Enter Root Data: "))
    if rootData == -1:
        return None
    root = GenericTreeNode(rootData)
    print("Enter number of children of ", rootData)
    childrenInput = int(input())

    for i in range(childrenInput):
        child = takeTreeInput()
        root.children.append(child)
    return root

def printTree(root):
    if root == None:
        return None
    print(root.data,":",end="")
    for child in root.children:
        print(child.data,end=",")
    print()

    for child in root.children:
        printTree(child)
    

root = takeTreeInput()
printTree(root)