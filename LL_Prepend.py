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

    # Define the prepend method for the LinkedList class
    def prepend(self, value):
        # Create a new Node with the given value
        new_node = Node(value)

        # Check if the linked list is empty
        if self.length == 0:
            # Set the head and tail attributes to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Set the next attribute of the new node to the current head
            new_node.next = self.head
            # Update the head attribute to the new node
            self.head = new_node

        # Increment the length attribute of the LinkedList
        self.length += 1

        # Return True to indicate a successful operation
        return True

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append('None')
        print('->'.join(values))

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp


my_linked_list = LinkedList(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.prepend(4)
my_linked_list.prepend(3)
my_linked_list.print()
print(my_linked_list.pop().value)
print(my_linked_list.pop().value)
print(my_linked_list.pop().value)
