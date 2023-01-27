# Linked Stack
class Node:
    def __init__(self, _data=None, _next=None):
        self.data = _data
        self.next = _next


class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, _data):
        new_node = Node(_data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if (not self.isEmpty()):
            return_value = self.top.data
            new_top = self.top.next
            self.top = new_top
            self.size -= 1
            return return_value
        else:
            print("Stack is empty")
            return -1

    def peek(self):
        return self.top.data

    def isEmpty(self):
        if (self.top == None):
            return True
        else:
            return False

    def show_stack(self):
        node_cursor = self.top
        print("<--Top-->")
        for i in range(self.size):
            print(node_cursor.data)
            node_cursor = node_cursor.next
        print("<--Bottom-->")


myLinkedStack = LinkedStack()

myLinkedStack.push("data1")
myLinkedStack.push("data2")
myLinkedStack.show_stack()
myLinkedStack.push("data3")
print(myLinkedStack.pop())
