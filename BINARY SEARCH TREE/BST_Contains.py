class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # Start by setting 'temp' to the root of the tree
        temp = self.root
    # Loop until 'temp' becomes None (end of tree)
        while (temp is not None):
            # If value to find is less than the current node's value
            if value < temp.value:
                # Move 'temp' to the left child and continue loop
                temp = temp.left
        # If value to find is greater than the current node's value
            elif value > temp.value:
                # Move 'temp' to the right child and continue loop
                temp = temp.right
        # If value is neither less nor greater, it must be equal
            else:
                # Value found! Return True.
                return True
    # If loop ends, value was not found in tree. Return False.
        return False


myBST = BinarySearchTree()
myBST.insert(2)
myBST.insert(1)
myBST.insert(3)
print(myBST.contains(5))
