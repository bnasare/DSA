class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def pop_first(self):
        # Check if the list is empty
        if self.length == 0:
            return None

    # Save a reference to the current head node
        temp = self.head

    # Update the head to the second node in the list
        self.head = self.head.next

    # Disconnect the removed node from the list
        temp.next = None

    # Decrease the length of the list by 1
        self.length -= 1

    # Check if the list is now empty
        if self.length == 0:
        # Set the tail to None if the list is empty
            self.tail = None

    # Return the removed node
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


my_linked_list = LinkedList(43)
my_linked_list.prepend(37)
print(my_linked_list.popFirst().value)
