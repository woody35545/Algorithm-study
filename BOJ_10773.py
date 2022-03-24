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
        old_top = self.top
        self.top = old_top.next
        self.size -= 1
        return old_top.value

    def isEmpty(self):
        return self.size == 0

def solve():
    myStack = Stack()
    N = int(input())

    for n in range(N):
        input_int = int(input())
        if input_int != 0:
            myStack.push(input_int)
        elif input_int == 0:
            myStack.pop()

    # 스택에 남아 있는 값들을 다 더해줌
    result = 0
    for i in range(myStack.size):
        result += myStack.pop()

    print(str(result))

solve()