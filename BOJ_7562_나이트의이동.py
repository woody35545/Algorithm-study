# 움직이는 경로 vector 선언해서 사용했는데 인덱스를 잘못계산해서 초기화해서 틀렸다. 움직일 수 있는 경로를 다시 확인해보는 습관을 들여야겠다.

from collections import deque
T = int(input())
I=0
graph = []
dir = [(-1,-2),(-2,-1),(-2,1),(-1,2),(2,-1),(1,-2),(2,1),(1,2)]
is_valid = lambda x,y : 0<=x<I and 0<=y<I
def bfs(graph, start:tuple):
    queue = deque([start])
    visited = [[False]*I for _ in range(I)]

    while queue:
        for i in range(len(queue)):
            cur_x, cur_y = queue.popleft()
            if visited[cur_x][cur_y] == False:
                visited[cur_x][cur_y] = True
                for k in range(len(dir)):
                    nx, ny =  cur_x + dir[k][0], cur_y + dir[k][1]

                    if is_valid(nx, ny) and visited[nx][ny] == False:
                        graph[nx][ny] = graph[cur_x][cur_y] + 1
                        queue.append((nx, ny))

def solve():
    global I,graph

    I = int(input())
    graph = [[0]*I for _ in range (I)]
    cur_x, cur_y = map(int,input().split())
    target_x, target_y = map(int,input().split())
    bfs(graph,(cur_x,cur_y))
    print(graph[target_x][target_y])


for _ in range(T):
    solve()
