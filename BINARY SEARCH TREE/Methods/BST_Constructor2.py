#! None has been assigned to the root of my BST, the insert method rather assigns a digit to the root of my BST.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


my_tree = BinarySearchTree()

print("Root:", my_tree.root)
