class Node:
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next


class Stack:
    def __init__(self):
        self.size = 0
        self.top = Node()

    def push(self, _value):
        new_top = Node(_value, self.top)
        self.top = new_top
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            old_top = self.top
            self.top = old_top.next
            return_value = old_top.value
            self.size -= 1
            return return_value

        else:
            return None

    def peek(self):
        return self.top.value

    def isEmpty(self):
        return self.size == 0

    def print_stack_one_line(self):
        for i in range(self.size):
            print(self.pop() , end = "")

def solve():
    input_str = input()
    stack = Stack()

    for i in range(len(input_str)):
        if stack.peek() != "<":
            if input_str[i] == "<":
                if stack.size > 0:
                    stack.print_stack_one_line()
                stack.push(input_str[i])
                print("<", end="")

            elif input_str[i] == " " and stack.size != 0:
                stack.print_stack_one_line()
                print(" ", end="")

            elif i == len(input_str)-1:
                stack.push(input_str[i])
                stack.print_stack_one_line()

            else:
                stack.push(input_str[i])

        elif stack.peek() == "<":
            if input_str[i] != ">":
                print(input_str[i], end="")
            elif input_str[i] == ">":
                print(input_str[i], end="")
                stack.pop()


solve()
