"""
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys


class ListQueue():
    def __init__(self):
        self.queue = []
        self.rear = 0
        self.front = 0

    def enqueue(self, _data):
        self.queue.append(_data)
        self.rear += 1

    def dequeue(self):
        if self.isEmpty() != 1:
            self.front += 1
            return self.queue[self.front - 1]
        else:
            return -1

    def size(self):
        return self.rear - self.front

    def isEmpty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
    def getFront(self) :
        if self.isEmpty() != 1:
            return self.queue[self.front]
        else:
            return -1

    def getBack(self):
        if self.isEmpty() != 1:
            return self.queue[self.rear-1]
        else:
            return -1

def solve():
    myListQueue = ListQueue()

    N = int(sys.stdin.readline().strip())

    for i in range(N):
        command_string = (sys.stdin.readline().rstrip()).split(" ")
        if command_string[0] == "push" :
            myListQueue.enqueue(int(command_string[1]))
        elif command_string[0] == "pop":
            print(myListQueue.dequeue())
        elif command_string[0] == "size":
            print(myListQueue.size())
        elif command_string[0] == "empty":
            print(myListQueue.isEmpty())
        elif command_string[0] == "front":
            print(myListQueue.getFront())
        elif command_string[0] == "back":
            print(myListQueue.getBack())


solve()

