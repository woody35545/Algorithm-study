from collections import deque
import sys

input = lambda : sys.stdin.readline().rstrip()
print = lambda x : sys.stdout.write(str(x))

N = int(input())
M = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def bfs(start):
    # start like '2:Node Number'
    queue = deque([start])
    visited = [False] * (N+1)
    res = []
    dist = 0

    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            if not visited[x]:
                if 0 < dist <= 2:
                    res.append(x)
                elif dist > 2:
                    break
                visited[x] = True

                for i in range(len(graph[x])):
                    if graph[x][i] == 1 and not visited[i]:
                        queue.append(i)

        dist += 1

    print(len(res))

    return len(res)

bfs(1)
