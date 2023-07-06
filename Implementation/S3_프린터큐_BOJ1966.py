T = int(input())

from collections import deque

def solve():
    global PRI, N, Q, documents

    queue = deque(documents)
    print(queue)
    print(len(queue))
    cnt = 1
    while queue:
        popped = queue.popleft() # doc_id, pri
        cur_doc_id = popped[0]
        cur_doc_pri = popped[1]

        # find current max priority
        current_max = -1
        for i in range(len(queue)):
            if current_max < queue[i][1]:
                current_max = queue[i][1]
        print(current_max)

        # 현재 popped 된 도큐먼트가 타겟이고, 바로 수행가능한 경우
        if cur_doc_id == Q and cur_doc_pri >= current_max:
            print(cnt)

        else:

            None


for i in range(T):
    N, Q = map(int, input().split(" "))
    PRI = deque(list(map(int, input().split(" "))))
    documents = []
    for i in range(len(PRI)):
        documents.append((i, PRI[i]))

    solve()
