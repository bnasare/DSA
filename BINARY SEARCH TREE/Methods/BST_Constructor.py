#! As usual, a digit has been assigned to the root of my BST

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node


myBST = BinarySearchTree(4)
print(myBST.root.value)
