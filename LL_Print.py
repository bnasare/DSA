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
    # Set a temporary pointer (temp) to the head of the list to start traversal
        temp = self.head

    # Iterate through the list until the end (temp is None)
        while temp is not None:
        # Print the value of the current node (temp)
            print(temp.value)

        # Move the temporary pointer (temp) to the next node in the list
            temp = temp.next