class GenericTreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

n1 = GenericTreeNode(10)
n2 = GenericTreeNode(1)
n3 = GenericTreeNode(2)
n4 = GenericTreeNode(3)
n5 = GenericTreeNode(4)
n6 = GenericTreeNode(5)
n7 = GenericTreeNode(6)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

n5.children.append(n6)
n6.children.append(n7)
