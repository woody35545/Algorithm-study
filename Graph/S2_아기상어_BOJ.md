**문제**: https://www.acmicpc.net/problem/17086  
**유형**: `그래프 이론`, `브루트포스 알고리즘`, `그래프 탐색`, `너비 우선 탐색`  

# Solved
```python
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

graph = [[0]*M for _ in range(N)]

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

# 그래프 초기화
for i in range(N):
    inputStr = sys.stdin.readline().rstrip().replace(" ", "")

    for j in range(len(inputStr)):
        graph[i][j] = int(inputStr[j])

def bfs(sx, sy):

    if graph[sx][sy] == 1:
        # 상어가 있는칸의 안전거리는 0
        return 0
    queue = deque([(sx, sy)])
    visited = [[-1]*M for _ in range(N)]
    visited[sx][sy] = 0


    while queue:
        cx, cy = queue.popleft()

        for i in range(len(dx)):

            nx, ny = cx + dx[i], cy + dy[i]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1:
                visited[nx][ny] = visited[cx][cy] + 1

                if graph[nx][ny] == 1:
                    return visited[nx][ny]

                queue.append((nx,ny))

cur_max = 0
# brute force
for r in range(N):
    for c in range(M):
        cur_max = max(cur_max, bfs(r,c))

sys.stdout.write(str(cur_max))
```
