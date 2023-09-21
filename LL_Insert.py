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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
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
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        # Check if index is out of bounds
        if index < 0 or index > self.length:
            return False
    # If index is 0, prepend the value
        if index == 0:
            return self.prepend(value)
    # If index is at the end, append the value
        if index == self.length:
            return self.append(value)
    # Create a new node with the value
        new_node = Node(value)
    # Get the node just before the insertion point
        temp = self.get(index - 1)
    # Set new_node's next to temp's next
        new_node.next = temp.next
    # Update temp's next to the new_node
        temp.next = new_node
    # Increment the length of the list
        self.length += 1
    # Return True as node inserted successfully
        return True


my_linked_list = LinkedList(1)
my_linked_list.append(3)


print('LL before insert():')
my_linked_list.print_list()


my_linked_list.insert(1, 2)

print('\nLL after insert(2) in middle:')
my_linked_list.print_list()


my_linked_list.insert(0, 0)

print('\nLL after insert(0) at beginning:')
my_linked_list.print_list()


my_linked_list.insert(4, 4)

print('\nLL after insert(4) at end:')
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    LL before insert():
    1
    3

    LL after insert(2) in middle:
    1
    2
    3

    LL after insert(0) at beginning:
    0
    1
    2
    3

    LL after insert(4) at end:
    0
    1
    2
    3
    4

"""