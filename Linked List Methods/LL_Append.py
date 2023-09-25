class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1


    def print_list(self):
        # Initialize an empty list to store the values of the nodes
        values = []
        # Start at the head of the list
        temp = self.head
        # Traverse the list until reaching a node that has no next node (i.e., the tail)
        while temp is not None:
            # Append the value of the current node to the list
            values.append(str(temp.value))
            # Move to the next node
            temp = temp.next
            # Append "None" to signify the end of the list
        values.append("None")
        # Print all values in the list, separated by " -> "
        print(" -> ".join(values))

    def append(self, value):
    # Create a new node with the given value
        new_node = Node(value)

    # Check to see if the linked list is empty
        if self.length is None:
        # Point both head and tail at the new node
            self.head = new_node
            self.tail = new_node
        else:
        # Point the next pointer of the last node at the new node
            self.tail.next = new_node
        # Point tail at the new node
            self.tail = new_node

    # Increment the length of the linked list
        self.length = +1

my_linked_list = LinkedList(7383)
my_linked_list.append(8)
my_linked_list.append(19)
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
my_linked_list.print_list()