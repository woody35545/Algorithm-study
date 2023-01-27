import sys

"""
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

"""


class Node:
    def __init__(self, _value, _next):
        self.value = _value
        self.next = _next

    def get_value(self):
        return self.value


class Stack:
    def __init__(self):
        self.last = None
        self.size = 0

    def push(self, _value):
        self.last = Node(_value, self.last)
        self.size += 1

    def pop(self):
        if (self.size != 0):
            res_value = self.last.value
            self.last = self.last.next
            self.size -= 1

            print(res_value)
        else:
            print("-1")

    def show(self):
        cur = self.last
        for i in range(self.size):
            print(cur.value)
            cur = cur.next

    def empty(self):
        if (self.size == 0):
            print("1")
        else:
            print("0")

    def top(self):
        if (self.size != 0):

            print(self.last.value)
        else:
            print("-1")


N = int(sys.stdin.readline())

new_stack = Stack()

for i in range(N):

    command_tokens = sys.stdin.readline().split(" ")
    command = command_tokens[0].replace("\n", "")
    if (command == "push"):
        new_stack.push(int(command_tokens[1]))
    elif (command == "top"):
        new_stack.top()
    elif (command == "empty"):
        new_stack.empty()
    elif (command == "pop"):
        new_stack.pop()
    elif (command == "size"):
        print(new_stack.size)
