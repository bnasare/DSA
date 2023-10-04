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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current is not None:
            num = num*2+current.value
            current = current.next
        return num


ll = LinkedList(1)
ll.prepend(1)
ll.prepend(0)
ll.prepend(0)
ll.prepend(1)

results = ll.binary_to_decimal()
print(results)
