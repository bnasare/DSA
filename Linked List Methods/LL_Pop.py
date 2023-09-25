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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def print(self):
        temp = self.head
        while(temp is not None):
            print(temp.value)
            temp = temp.next

    def pop(self):
    # Check if the list is empty
        if self.length == 0:
            return None
    # Initialize temp and pre to the head
        temp = self.head
        pre = self.head
    # Iterate until the last node
        while(temp.next):
            pre = temp
            temp = temp.next
    # Set the new tail to the previous node
        self.tail = pre
    # Remove link to the removed node
        self.tail.next = None
    # Decrement list length by 1
        self.length -= 1
    # Check if the list is now empty
        if self.length == 0:
        # Set head and tail to None
            self.head = None
            self.tail = None
    # Return the removed node
        return temp



my_linked_list = LinkedList(4)
my_linked_list.append(98)

print(my_linked_list.pop().value)
print(my_linked_list.pop().value)
print(my_linked_list.pop())