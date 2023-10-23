class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Create a new node with the provided value
        new_node = Node(value)

    # Check if the tree is empty
        if self.root is None:
            # Make the new node the root and return True
            self.root = new_node
            return True
    # Start at the root of the tree
        temp = self.root
    # Loop until the correct spot is found
        while (True):
            # Check for duplicate values
            if new_node.value == temp.value:
                # Duplicate found, return False
                return False
        # Check if the new value is less than current node's value
            if new_node.value < temp.value:
                # Is the left child spot empty?
                if temp.left is None:
                    # Insert new node as left child, return True
                    temp.left = new_node
                    return True
            # If not empty, move to left child
                temp = temp.left
        # If new value is greater, go to the right child
            else:
                # Is the right child spot empty?
                if temp.right is None:
                    # Insert new node as right child, return True
                    temp.right = new_node
                    return True
            # If not empty, move to right child
                temp = temp.right


myBST = BinarySearchTree()
myBST.insert(2)
myBST.insert(1)
myBST.insert(3)
print(myBST.root.value)
print(myBST.root.left.value)
print(myBST.root.right.value)
