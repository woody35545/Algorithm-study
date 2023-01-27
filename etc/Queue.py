# Queue는 기본적으로 Rear로 들어와서(EnQueue) Front로 나가는(DeQueue) 구조임

class listQueue():

    def __init__(self):
        self.queue = []

    def enqueue(self, _data: int):
        self.queue.append(_data)

    def dequeue(self):
        dequeued_object = None
        if not self.isEmpty():
            dequeued_object = self.queue[0]
            self.queue = self.queue[1:]
        return dequeued_object

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return None

    def isEmpty(self):
        if len(self.queue) > 0:
            return True

        return False

    def showQueue(self):
        print(f"<REAR> ", end="")
        for i in range(len(self.queue)):
            print(f"[{i}] {self.queue[i]} ", end="")
        print(f"<FRONT> ", end="\n")


class ListQueue2():
    def __init__(self):
        self.queue = []
        self.rear = 0
        self.front = 0

    def enqueue(self, _data):
        self.queue.append(_data)
        self.rear += 1

    def dequeue(self):
        if not self.isEmpty():
            return_value = self.queue[self.front]
            self.front += 1
            return return_value
        else:
            return None

    def size(self):
        return self.rear - self.front

    def isEmpty(self):
        if self.size == 0:
            return True
        return False


def test_queue():
    myListQueue = listQueue()

    myListQueue.enqueue(1)
    myListQueue.enqueue(2)
    myListQueue.enqueue(5)
    myListQueue.showQueue()


test_queue()
