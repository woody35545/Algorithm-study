import sys

input = sys.stdin.readline

class Edge:
    start_vertex = 0
    end_vertex = 0
    cost = 0

    def __init__(self, sv, ev, c):
        self.start_vertex = sv
        self.end_vertex = ev
        self.cost = c

INF = sys.maxsize
edge_list = []
N, M = map(int, input().split(" "))

min_dist = [INF] * (N+1)
# 시작 vertex의 min_dist 값을 0으로 초기화, 시작 vertex = 1
min_dist[1] = 0

for i in range(M):
    start_vertex, end_vertex, cost = map(int, input().split(" "))
    edge_list.append(Edge(start_vertex, end_vertex, cost))

for _ in range(N-1):
    for edge in edge_list:
        if min_dist[edge.start_vertex] != INF and min_dist[edge.end_vertex] > min_dist[edge.start_vertex] + edge.cost:
            min_dist[edge.end_vertex] = min_dist[edge.start_vertex] + edge.cost


neg_cycle = False
# 만약 업데이트가 또 발생할 경우 음수 사이클이 존재함을 의미
for _ in range(N-1):
    for edge in edge_list:
        if min_dist[edge.start_vertex] != INF and min_dist[edge.end_vertex] > min_dist[edge.start_vertex] + edge.cost:
            neg_cycle = True

if neg_cycle:
    print(-1)

else:
    for i in range(2,N+1):
        print(min_dist[i]) if min_dist[i] != INF else print(-1)
