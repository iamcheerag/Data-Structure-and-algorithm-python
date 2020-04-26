"""
Is node present?

Given a Binary Tree and an integer x, check if node with data x is present in the input binary tree or not. Return true or false.
Input format :
Line 1 : Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)
Line 2 : Integer x

Output Format :
true or false
"""


class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    root = int(input())
    if root == -1:
        return

    btn = BinaryTree(root)
    leftTree = takeInput()
    rightTree = takeInput()
    btn.left = leftTree
    btn.right = rightTree
    
    return btn

def isNodePresent(root,x):
    if root is None:
        return

    if root.data == x:
        return True
    result = isNodePresent(root.left,  x)
    if result:
        return True
    
    result = isNodePresent(root.right, x)
    if result :
        return True

def printTree(root):
    if root is None:
        return
    
    print(root.data)
    printTree(root.left)
    printTree(root.right)

root = takeInput()
#printTree(root)

result = isNodePresent(root, 5)
if result is True:
    print("true")
else:
    print("false")