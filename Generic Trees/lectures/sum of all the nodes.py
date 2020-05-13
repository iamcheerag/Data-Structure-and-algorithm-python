"""
Sum of all nodes
Send Feedback
Given a generic tree, count and return the sum of all nodes present in the given tree.
Input format :
Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
Output Format :
Sum of all nodes
Sample Input :
10 3 20 30 40 2 40 50 0 0 0 0 
Sample Output :
190

"""
class GenericTree:
    def __init__(self,data):
        self.data = data
        self.children = []

def takeInput():
    print("Enter root :")
    rootData = int(input())    
    if rootData == -1:
        return None
    root = GenericTree(rootData)

    print("Enter the no of children of ",rootData)
    rootchild = int(input())

    for i in range(rootchild):
        child = takeInput()
        root.children.append(child)
    return root

def printGenericTree(root):
    if root == None:  # edge case not the base case
        return None

    print(root.data,":",end = "")
    for child in root.children:
        print(child.data,end= ",")
    print()

    for child in root.children:
        printGenericTree(child)
        
def sumofNodes(root):
    if root == None:
        return 0
    sum = root.data
    for child in root.children:
        sum = sum + sumofNodes(child)
    return sum

root =  takeInput()
# n1 = GenericTree(10)
# n2 = GenericTree(2)
# n3 = GenericTree(3)

# n1.children.append(n2)
# n1.children.append(n3)

printGenericTree(root)
print("====================")
print(sumofNodes(root))