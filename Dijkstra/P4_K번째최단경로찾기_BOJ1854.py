from queue import PriorityQueue
import sys
input = sys.stdin.readline

# 1번 노드가 시작 노드
START_NODE = 1

N, M, K = map(int, input().split(" "))

# list graph
G = [[] for _ in range(N+1)]

MIN_DIST = [[sys.maxsize]*K for _ in range(N+1)]

for i in range(M):
    # vertex a to vertex b
    va, vb, cost = map(int, input().split(" "))
    G[va].append((vb,cost))

# 우선순위 큐 초기화
pq = PriorityQueue()
# 1번 노드의 1번째 최소거리는 0으로 초기화
MIN_DIST[START_NODE][0] = 0
pq.put((MIN_DIST[1][0], START_NODE))

while pq.qsize() > 0:
    popped = pq.get()
    # cv: current vertex, cc: current_cost
    cc = popped[0]
    cv = popped[1]

    for nv, nc in G[cv]:
        newCost = cc + nc
        if MIN_DIST[nv][K-1] > newCost:
            MIN_DIST[nv][K-1] = newCost
            MIN_DIST[nv].sort()
            pq.put((newCost, nv))

for i in range(1, N+1):
    if MIN_DIST[i][K-1] == sys.maxsize:
        print(-1)
    else:
        print(MIN_DIST[i][K-1])
