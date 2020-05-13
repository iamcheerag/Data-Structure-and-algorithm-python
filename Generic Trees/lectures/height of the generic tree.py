class GenericTree:
    def __init__(self,data):
        self.data = data
        self.children = []


def takeTreeInput():
    rootData = int(input("Enter root: "))
    if rootData == -1:
        return
    root = GenericTree(rootData)
    print("No of children of ",rootData)
    childNode = int(input())

    for i in range(childNode):
        childRoot = takeTreeInput()
        root.children.append(childRoot)
    
    return root

def heightOfGenericTree(root):
    if root == None:
        return 0
    rootHeight = 0
    for child in root.children:
        childHeight = heightOfGenericTree(child)
        rootHeight = max(rootHeight,childHeight)
    return rootHeight + 1


#root = takeTreeInput()
root = GenericTree(10)
child1 = GenericTree(1)
child2 = GenericTree(2)
child3 = GenericTree(3)
child4 = GenericTree(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)
child3.children.append(child4)


print(heightOfGenericTree(root))
