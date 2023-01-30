'''
답은 맞는데 계속 시간초과 생겨서 여러방면으로 확인해보니 pypy로 돌려서 시간초과가 발생한 것이었다. pypy가 python3 보다 빠르다고 하는데 해당 문제는 python3로 했을 때만 채점기준을 만족하였고, 같은 코드여도 
pypy로 채점했을 경우 시간 초과가 발생하였다. 정확한 원인을 찾아봐야 할 것 같다
'''
from queue import PriorityQueue
import sys
input = lambda : sys.stdin.readline().rstrip()
p = lambda x: sys.stdout.write(str(x) +  "\n")

# cV: 노드 수, cE: 엣지 수
cV, cE = map(int, input().split())
# start_vertex: 출발 노드
start_vertex = int(input())

# start vertex 기준으로 각 노드(인덱스)까지의 최소 비용을 저장하고 있는 리스트
# 초기에는 가장 큰 값인 INF로 초기화
min_costs = [sys.maxsize] * (cV + 1)
# 초기 시작 vertex의 cost는 0 이므로 0으로 초기화
min_costs[start_vertex] = 0

# 그래프 탐색에서 방문을 기록하기 위한 리스트
visited = [False] * (cV+1)

# 노드 연결관계를 저장할 리스트 선언
graph = [[] for _ in range(cV+1)] # 노드 번호: 1 <= Node Number <= 20,000

# Priority Queue 초기화
priority_queue = PriorityQueue()

for i in range(cE):
    # u에서 v로 가는 간선, cost = w
    u, v, w = map(int, input().split())
    # adjancency list graph에 u에서 v로 가는 cost = w 인 간선 정보 추가
    graph[u].append((v,w))

# PriorityQueue(cost, vertex) 이므로 시작점 추가
priority_queue.put((0, start_vertex))


while priority_queue.qsize() >0:
    current_popped = priority_queue.get() # cur_popped like (cost, vertex_number)
    current_vertex = current_popped[1]

    #if not visited[current_vertex]:
    if visited[current_vertex]:
        continue
    visited[current_vertex] = True

    for neighbor_data in graph[current_vertex]:
        neighbor_vertex = neighbor_data[0]
        neighbor_cost = neighbor_data[1]

        if min_costs[neighbor_vertex] > min_costs[current_vertex] + neighbor_cost:
            min_costs[neighbor_vertex] = min_costs[current_vertex] + neighbor_cost
            priority_queue.put((min_costs[neighbor_vertex], neighbor_vertex))

[p(min_costs[i]) if visited[i] else p("INF") for i in range(1,len(min_costs))]
