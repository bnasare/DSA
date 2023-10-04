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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        return ' -> '.join(values)

    def find_middle_node(self):
        # 1. Initialize two pointers: 'slow' and 'fast',
        # both starting from the head.
        slow = self.head
        fast = self.head

    # 2. Iterate as long as 'fast' pointer and its next
    # node are not None.
    # This ensures we don't get an error trying to access
    # a non-existent node.
        while fast is not None and fast.next is not None:

        # 2.1. Move 'slow' one step ahead.
        # This covers half the distance that 'fast' covers.
            slow = slow.next

        # 2.2. Move 'fast' two steps ahead.
        # Thus, when 'fast' reaches the end, 'slow'
        # will be at the middle.
            fast = fast.next.next

    # 3. By now, 'fast' has reached or surpassed the end,
    # and 'slow' is positioned at the middle node.
    # Return the 'slow' pointer, which points to
    # the middle node.
        return slow


my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.prepend(5)
my_linked_list.prepend(6)
print(my_linked_list.print_list())
print(my_linked_list.find_middle_node().value)
