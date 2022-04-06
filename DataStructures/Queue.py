# Queue는 기본적으로 Rear로 들어와서(EnQueue) Front로 나가는(DeQueue) 구조임

class listQueue():
   
    def __init__(self):
        self.queue = []
    
    def enqueue(self,_data:int):
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
        print(f"<REAR> ",end = "")
        for i in range(len(self.queue)):
            print(f"[{i}] {self.queue[i]} ", end = "")
        print(f"<FRONT> ",end = "\n")
def test_queue(): 
    
    myListQueue = listQueue()
    
    myListQueue.enqueue(1)
    myListQueue.enqueue(2)
    myListQueue.enqueue(5)
    myListQueue.showQueue()
    

test_queue()
