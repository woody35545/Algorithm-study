# Category topological sort

from collections import deque
N, M = map(int, input().split(" "))

#graph = [[0]*(N+1) for _ in range(N+1)]
list_graph =[[] for _ in range(N+1)]
indegree = [0] * (N+1)


for i in range(M):
    a,b = map(int, input().split(" "))
    # graph[a][b] = 1
    # graph[b][a] = 1
    list_graph[a].append(b)
    indegree[b] += 1

queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    popped = queue.popleft()
    print(str(popped), end=" ")
    # for i in range(1, len(graph[popped])):
    #
    #     if graph[popped][i] == 1:
    #         indegree[i] -= 1
    for neighbor in list_graph[popped]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

