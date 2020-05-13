class GenericTree:
    def __init__(self,data):
        self.data = data
        self.children = []

def takeInput():
    rootData = int(input("Enter root:"))
    if rootData == -1:
        return None
    
    root = GenericTree(rootData)
    print("Enter Number of children for",rootData)
    childInput = int(input())

    for i in range(childInput):
        child = takeInput()
        root.children.append(child)
    return root


def NodeWithLargestData(root):
    if root == None:
        return 

    curr = root.data

    for childRoot in root.children:
        childData = NodeWithLargestData(childRoot)
        curr = max(childData, curr)
    return curr


root = takeInput()
print(NodeWithLargestData(root))