class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node

        for _ in range(start_index):
            previous_node = previous_node.next

        current_node = previous_node.next

        for _ in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move

        self.head = dummy_node.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


# """
#     EXPECTED OUTPUT:
#     ----------------
#     Original linked list:
#     1
#     2
#     3
#     4
#     5
#     Reversed sublist (2, 4):
#     1
#     2
#     5
#     4
#     3
#     Reversed entire linked list:
#     3
#     4
#     5
#     2
#     1
#     Reversed sublist of length 1 (3, 3):
#     3
#     4
#     5
#     2
#     1
#     Reversed empty linked list:
#     None

# """


# def reverse_between(self, start_index, end_index):
#     # If there's only one node or no nodes at all, we don't need to do anything.
#     # In our case, we have 8 nodes, so we can continue.
#     if self.length <= 1:
#         return

#     # We create a dummy node to help us keep track of the start of our linked list.
#     # Think of it as a helper that points to the first node (1 in our case).
#     dummy_node = Node(0)
#     dummy_node.next = self.head
#     previous_node = dummy_node

#     # We move our 'previous_node' to the node just before where we want to start reversing.
#     # In our case, we want to start reversing from position 3 (node with value 3),
#     # so 'previous_node' will point to node 2.
#     for i in range(start_index):
#         previous_node = previous_node.next

#     # 'current_node' is the first node we want to reverse.
#     # So it points to node 3 in our case.
#     current_node = previous_node.next

#     # Now we start reversing the nodes.
#     for i in range(end_index - start_index):
#         # 'node_to_move' is the next node we want to move to the front.
#         # Initially, it points to node 4.
#         node_to_move = current_node.next
#         # We detach 'node_to_move' from the list and move 'current_node' to the next node.
#         current_node.next = node_to_move.next
#         # We then put 'node_to_move' in front of the already reversed nodes.
#         node_to_move.next = previous_node.next
#         # And then we update 'previous_node' to point to our newly moved node.
#         previous_node.next = node_to_move

#     # At the end, we update the start of our linked list.
#     self.head = dummy_node.next


# # Let's say current_node is at node 3 and previous_node is at node 2 initially.

# node_to_move = current_node.next  # node_to_move is now at node 4.

# # We detach 'node_to_move' (node 4) from the list and move 'current_node' (node 3) to the next node (node 5).
# current_node.next = node_to_move.next

# # We then put 'node_to_move' (node 4) in front of the already reversed nodes.
# # Since no nodes have been reversed yet, 'node_to_move' just goes in front of 'current_node' (node 3).
# node_to_move.next = previous_node.next

# # And then we update 'previous_node' (node 2) to point to our newly moved node (node 4).
# previous_node.next = node_to_move

# # Now, our linked list looks like this: 1->2->4->3->5->6->7->8
# # And we repeat this process for nodes 5 and 6.

# # At the end, we update the start of our linked list.
# self.head = dummy_node.next


# I see where the confusion is coming from. Let's clarify:

# When we say "`node_to_move` (node 4)", we're referring to the node itself, which has the value 4. This doesn't change throughout the process.

# When we do `current_node.next = node_to_move.next`, we're not changing `node_to_move` itself, but rather we're changing what `current_node` (node 3) points to next. After this line, `current_node` (node 3) points to node 5.

# When we do `node_to_move.next = previous_node.next`, we're changing what `node_to_move` (node 4) points to next. After this line, `node_to_move` (node 4) points to what `previous_node` (node 2) was pointing to before, which is node 3.

# So, even though we've changed what `node_to_move` points to next, `node_to_move` itself is still the node with the value 4.

# I hope this clears up the confusion! 😊
