class Node():
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next

    def get_value(self):
        return self.value


class Stack():
    def __init__(self):
        self.size = 0
        self.top = Node()

    def push(self, _value):
        new_top = Node(_value, self.top)
        self.top = new_top
        self.size += 1

    def pop(self):
        old_top = self.top
        self.top = self.top.next

        self.size -= 1

        return old_top.get_value()

    def peek(self):
        return self.top.value

    def is_empty(self):
        return self.size == 0

    def reset(self):
        self.size = 0
        self.top = Node()


def solve():
    stack = Stack()

    while True:
        res = "no"
        stack.reset()
        input_str = input().rstrip()
        if len(input_str) == 1 and input_str[0] == ".":
            # 종료 문자 들어오면 종료
            break
        else:
            for i in range(len(input_str)):
                if input_str[i] == "(" or input_str[i] == "[":
                    stack.push(input_str[i])
                elif input_str[i] == ")":
                    if stack.peek() == "(":
                        stack.pop()
                    else:
                        stack.push(input_str[i])
                        res = "no"

                elif input_str[i] == "]":
                    if stack.peek() == "[":
                        stack.pop()
                    else:
                        stack.push(input_str[i])
                        res = "no"

            if not stack.is_empty():
                res = "no"
            else:
                res = "yes"

            print(res)


solve()
