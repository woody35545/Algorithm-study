class ListQueue():
    def __init__(self):
        self.queue = []
        self.rear = 0  # 다음 들어올 데이터가 들어갈 Index 를 가리키고 있는 포인터
        self.front = 0 # 다음 출력할 데이터를 가리키는 포인터

    def enqueue(self, _data):
        self.queue.append(_data)
        self.rear += 1

    def dequeue(self):
        if not self.isEmpty():
            return_value = self.queue[self.front]
            self.front += 1 # 프론트 포인터를 하나씩 이동시킴
            return return_value

        return None

    def isEmpty(self):
        if self.front == self.rear:
        # front 값이 rear-1 이면 출력할 값이 없음을 의미
            return True
        return False

    def size(self):
        return self.rear - self.front

def solve():
    ## Queue 를 이용했을 때 시간초과가 발생했음

    # result list
    res_list = []

    # make Queue
    myListQueue = ListQueue()

    # init inputs 
    N, K = [int(x) for x in input().split(" ")]

    # init Queue
    for i in range(N):
        myListQueue.enqueue(i + 1)

    # complete result list
    while not myListQueue.isEmpty():
        for i in range(K):
            val = myListQueue.dequeue()
            if i == K - 1:
                res_list.append(val)
            else:
                myListQueue.enqueue(val)

    # print(myListQueue.queue)
    # print(res_list)

    # print res_list
    print("<", end="")
    for i in range(len(res_list)):
        print(f"{res_list[i]}", end="")
        if i != (len(res_list) - 1):
            print(", ", end="")
        else:
            print(">", end="")

    


solve()
