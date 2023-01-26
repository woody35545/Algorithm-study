from collections import deque
import sys

input = lambda : sys.stdin.readline().rstrip()
print = lambda x : sys.stdout.write(str(x))

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
counts = [0] * (N+1) # index: Node Num, Value: Infection Total Count

for i in range(M):
    a,b = map(int,input().split())
    # Directed Graph
    #if not a==b:
    graph[b].append(a)


def bfs(start):
    # start like '2:Node Number'
    queue = deque([start])
    visited = [False] * (N+1)
    res = []

    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            if not visited[x]:
                res.append(x)
                visited[x] = True

                for i in range(len(graph[x])):
                    if not visited[graph[x][i]]:
                        queue.append(graph[x][i])

    return len(res)

for i in range(1,N+1):
    counts[i] = bfs(i)

max_count = max(counts)
res = []


for i in range(len(counts)):
    if counts[i] == max_count:
        res.append(i)

res.sort()

answer = ""
for i in res:
    answer += str(i) + " "

print(answer.rstrip())
