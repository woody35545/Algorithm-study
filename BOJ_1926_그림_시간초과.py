'''
어디서 시간복잡도를 줄여야할지 아직 못찾음
'''

from collections import deque
import sys


sys_input = lambda : sys.stdin.readline().rstrip()

DIR = [(-1,0),(1,0),(0,-1),(0,1)]

ROWS, COLS = map(int, sys_input().split())

#graph = [[0]*COLS for _ in range(ROWS)]
graph = []
visited = [[0]*COLS for _ in range(ROWS)]

section_count = 0
section_sizes = []

for i in range(ROWS):
    #graph[i] = list(map(int,sys_input().split()))
    graph.append(list(map(int,sys_input().split())))
def find_next():
    for i in range(ROWS):
        for j in range(COLS):
            if graph[i][j] == 1 and not visited[i][j]:
                return i,j

    return -1,-1

def bfs(start):
    global visited, section_count,section_sizes
    queue = deque([start])
    size_count = 0
    while queue:
        x,y = queue.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            size_count += 1
            for i in range(len(DIR)):
                nx,ny = x + DIR[i][0], y + DIR[i][1]

                if 0 <= nx < ROWS and 0 <= ny < COLS and graph[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx,ny))

    section_count += 1
    section_sizes.append(size_count)


sx,sy = find_next()
while sx != -1:
    bfs((sx,sy))
    sx, sy = find_next()

if section_count != 0:
    print(section_count)
    print(max(section_sizes), end = '')
else:
    print(section_count)
    print(0, end='')


