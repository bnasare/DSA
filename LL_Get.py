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

    def get(self, index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp

    def append(self, value):
        new_node=Node(value)
        if self.length is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

my_linked_list=LinkedList(9)
my_linked_list.append(3)
my_linked_list.append(8)
my_linked_list.append(38)

print(my_linked_list.get(2).value)
