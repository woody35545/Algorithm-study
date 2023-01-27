from collections import deque
import sys

T = int(input())
R,C,K = 0,0,0
graph = []
found = []
need_to_find = 0
bfs_search_count = 0

search_dir = [(1,0),(-1,0),(0,1),(0,-1)]

def init_input():
    global graph, need_to_find, found, bfs_search_count, R,C,K

    R, C, K = map(int, sys.stdin.readline().rstrip().split(" "))
    need_to_find = 0
    bfs_search_count = 0
    found = [[False] * C for _ in range(R)]
    graph = [[0] * C for _ in range(R)]

    for _ in range(K):
        r, c = map(int, sys.stdin.readline().rstrip().split(" "))
        graph[r][c] = 1
        need_to_find += 1


def find_next_start_vertex(graph):
    global R,C,found
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 1 and not found[i][j]:
                return (i,j)
    return (-1,-1)

def bfs(graph, start):

    global bfs_search_count, found, need_to_find
    queue = deque([(start[0],start[1])])
    visited = [[False] * C for _ in range(R)]

    while queue:

        cx, cy = queue.popleft()
        
        if not visited[cx][cy]:
            
            visited[cx][cy] = True
            found[cx][cy] = True
            need_to_find -= 1

            for dir in search_dir:
                nx, ny = cx + dir[0], cy + dir[1]

                if 0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append((nx, ny))
    bfs_search_count += 1


def solve():

    while need_to_find > 0:
        start_vertex = find_next_start_vertex(graph)
        if start_vertex != (-1,-1):
            bfs(graph, start_vertex )

    print(bfs_search_count)
    
for i in range(T):
    init_input()
    solve()
