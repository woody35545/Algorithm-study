from collections import deque
import sys

input = lambda : sys.stdin.readline().rstrip()
print = lambda x : sys.stdout.write(str(x))

N = int(input())
start, end = map(int,input().split())
M = int(input())

graph = [[0]*(N+1) for _ in range(N+1)] # 1 <= node_num <= 100

for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def bfs(start,end):
    # start like '2:Node Number'
    queue = deque([start])
    visited = [False] * (N+1)
    dist = 0

    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            if not visited[x]:
                if x == end:
                    return dist

                visited[x] = True

                for i in range(len(graph[x])):
                    if graph[x][i] == 1 and not visited[i]:
                        queue.append(i)

        dist += 1

    return -1 # means target not reachable

print(bfs(start,end))
