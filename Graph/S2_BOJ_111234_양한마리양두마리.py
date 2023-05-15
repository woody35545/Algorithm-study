from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(start: tuple):
    global count, H, W
    d = deque([start])
    graph[start[1]][start[0]] = '.'  # 방문 표시

    while d:
        px, py = d.popleft()

        for k in range(len(DIR)):
            nx, ny = px + DIR[k][0], py + DIR[k][1]
            if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] == '#':
                d.append((nx, ny))
                graph[ny][nx] = '.'  # 방문 표시


for _ in range(T):
    H, W = map(int, input().split())

    # init graph and count
    graph = [list(input().rstrip()) for _ in range(H)]
    count = 0

    for p in range(H):
        for q in range(W):
            if graph[p][q] == '#':
                count += 1
                bfs((q, p))

    sys.stdout.write(str(count) + "\n")


"""
# 아래 코드는 시간초과 발생함

from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(start: tuple):
    global visited, count, H, W
    d = deque([(start[0], start[1])])

    while (len(d) > 0):
        px, py = d.popleft()
        #print(f"popped, px: {px}, py: {py}")
        #print(visited)
        if not visited[py][px]:
            visited[py][px] = True  # update visited

        for k in range(len(DIR)):
            nx, ny = px + DIR[k][0], py + DIR[k][1]
            #print(f"nx, ny: {nx}, {ny}")
            if 0 <= nx < W and 0 <= ny < H and not visited[ny][nx] and graph[ny][nx] == '#':
                #print(f"append, nx: {nx}, ny: {ny}")
                d.append((nx, ny))


for i in range(T):
    H, W = map(int, input().split(" "))
    #print(f"H,W: {H}, {W}")

    # init graph
    graph = [[""] * W for _ in range(H)]
    for h in range(H):
        input_str = input()
        for w in range(W):
            graph[h][w] = input_str[w]

    # init visited
    visited = [[False] * W for _ in range(H)]

    # init count
    count = 0

    # find position
    for p in range(H):
        for q in range(W):
            if not visited[p][q] and graph[p][q] == '#':
                count += 1
                bfs((q, p))

    sys.stdout.write(str(count)+"\n")
"""
