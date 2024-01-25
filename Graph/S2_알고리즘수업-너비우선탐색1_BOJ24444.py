from collections import deque
import sys

N,M,R = map(int,sys.stdin.readline().rstrip().split(" "))

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[a].append(b)
    graph[b].append(a)
    
result = [0] * (N + 1)


def bfs(start):
    queue = deque([start])
    visited = [False] * (N+1)
    visited[start] = True
    order = 1

    while queue:
        cv = queue.popleft()
        result[cv] = order
        order += 1

        candidates = []
        for nv in graph[cv]:
            if not visited[nv]:
                visited[nv] = True
                candidates.append(nv)

        # 오름차순으로 출력하기 위함
        candidates.sort()
        queue.extend(candidates)

bfs(R)

for i in range(1 , len(result)):
    sys.stdout.write(str(result[i]) + '\n')
