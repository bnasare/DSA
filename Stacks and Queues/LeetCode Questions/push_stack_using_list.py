class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for values in self.stack_list:
            print(values)

    def push(self, value):
        self.stack_list.append(value)


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.print_stack()
