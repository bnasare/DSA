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


def find_nth_node_from_end(ll, k):
    slow = fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast is not None:
            slow = slow.next
            fast = fast.next
    return slow


my_linked_list = LinkedList(3)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.prepend(7)
my_linked_list.prepend(1)
my_linked_list.prepend(91)

k = 2
result = find_nth_node_from_end(my_linked_list, k)
print(result.value)
