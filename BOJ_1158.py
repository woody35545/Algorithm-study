class ListQueue():
    def __init__(self):
        self.queue = []
        
    def enqueue(self,_data):
        self.queue.append(_data)

    def dequeue(self):
        if not self.isEmpty():
            return_value = self.queue[0]
            self.queue = self.queue[1:]
            return return_value
    
        return None

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    def size(self):
        return len(self.queue)

class Node():
    def __init__(self,_prev, _next, _data):
        self.prev = _prev
        self.next = _next
        self.data = _data

class LinekdQueue():
    def __init__(self):
        self.queue = None
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
        myListQueue.enqueue(i+1)
    
    # complete result list
    while not myListQueue.isEmpty():
        for i in range(K):
            val = myListQueue.dequeue()
            if i == K-1:
                res_list.append(val)
            else:
                myListQueue.enqueue(val)
   
    #print(myListQueue.queue)
    #print(res_list)
    
    # print res_list
    print("<" , end ="")
    for i in range(len(res_list)): 
        print(f"{res_list[i]}", end = "")
        if i != (len(res_list)-1):
            print(" ", end = "")
        else:
            print(">" , end = "")
    
    return 


def solve2():
    input_list = []
    # Queue를 이용하지 않고 풀기
    N, K = [int(x) for x in input().split(" ")]
    for i in range(N):
        input_list.append(i+1)

solve()
