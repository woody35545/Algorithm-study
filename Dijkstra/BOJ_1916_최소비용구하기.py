import sys
from queue import PriorityQueue

input = sys.stdin.readline
fprint = sys.stdout.write

N = int(input())
M = int(input())

# 1 <= N <= 1000 이므로 N+1로 선언
list_graph = [[] for _ in range(N+1)]

min_dist = [sys.maxsize] * (N+1)

visited = [False] * (N+1)

for i in range(M):
    # va: start vertex
    # vb: end vertex
    va, vb, cost = map(int, input().split(" "))

    list_graph[va].append((vb,cost))

qStart, qEnd = map(int, input().split(" "))

def dijkstra(start, end):
    global min_dist, visited
    pq = PriorityQueue()

    pq.put((0,start))

    min_dist[start] = 0

    while pq.qsize() > 0:
        popped = pq.get()
        cur_vertex = popped[1]

        if visited[cur_vertex]:
            continue

        visited[cur_vertex] = True

        for next in list_graph[cur_vertex]:
            neighbor_vertex, cost = next

            if visited[neighbor_vertex]:
                continue

            if min_dist[neighbor_vertex] > min_dist[cur_vertex] + cost:
                min_dist[neighbor_vertex] = min_dist[cur_vertex] + cost
                pq.put((min_dist[neighbor_vertex], neighbor_vertex))

    return min_dist[end]

fprint(str(dijkstra(qStart,qEnd)))
