class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for values in self.stack_list:
            print(values)

    def is_empty(self):
        return len(self.stack_list) == 0

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def reverse_string(string):
    # create a new stack
    stack = Stack()
    # create an empty string to store the reversed string
    reversed_string = ""

    # push each character in the string onto the stack
    for char in string:
        stack.push(char)

    # pop each character off the stack and append it to the reversed string
    while not stack.is_empty():
        reversed_string += stack.pop() # type: ignore

    # return the reversed string
    return reversed_string


my_string = 'm u m m y'

print(reverse_string(my_string))
