class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        values = []
        temp = self.first
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        print(' -> '.join(values))


my_queue = Queue(3)
my_queue.print_queue()
