from collections import deque
import sys
N = int(sys.stdin.readline().rstrip())

sx, sy, tx, ty = map(int, sys.stdin.readline().rstrip().split(" "))

dx = [-2, -2, 0, 0, 2, 2 ]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(sx, sy):
    queue = deque([(sx,sy)])
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True
    count = 0

    while queue:
        for _ in range(len(queue)):

            cx, cy = queue.popleft()

            if cx == tx and cy == ty:
                return count

            for i in range(len(dx)):
                nx, ny = cx + dx[i], cy + dy[i]

                if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

        count +=1
    return -1

sys.stdout.write(str(bfs(sx,sy)))
