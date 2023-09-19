# Define the Node class for a singly linked list
class Node:
    # Constructor for the Node class
    def __init__(self, value):
        # Set the value attribute for the Node
        self.value = value
        # Initialize the next attribute to None
        self.next = None

# Define the LinkedList class
class LinkedList:
    # Constructor for the LinkedList class
    def __init__(self, value):
        # Create a new Node with the given value
        new_node = Node(value)
        # Set the head attribute to the new Node
        self.head = new_node
        # Set the tail attribute to the new Node
        self.tail = new_node
        # Initialize the length attribute to 1
        self.length = 1

my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)