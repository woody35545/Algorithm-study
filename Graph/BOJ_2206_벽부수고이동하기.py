from collections import deque
import sys
sys_in = lambda : sys.stdin.readline().rstrip()
sys_out = lambda x : sys.stdout.write(str(x))
# notations
WALL = 1

ROWS, COLS = map(int,sys_in().split())

DIR = [(1,0),(-1,0),(0,1),(0,-1)]

WALLS = []

# init original map
original_graph = [[0]*COLS for _ in range(ROWS)]

for i in range(ROWS):
    current_row = sys_in()
    for j in range(COLS):
        current_value = int(current_row[j])
        if current_value == WALL:
            WALLS.append((i,j))
        original_graph[i][j] = current_value

def bfs(graph,start):
    queue = deque([start])
    cost = [[0]*COLS for _ in range(ROWS)]
    visited = [[False]*COLS for _ in range(ROWS)]

    while queue:
        x,y = queue.popleft()
        if not visited[x][y]:
            visited[x][y] = True

            for i in range(len(DIR)):
                nx, ny = x + DIR[i][0], y + DIR[i][1]

                if 0 <= nx < ROWS and 0 <= ny < COLS and graph[nx][ny] != 1 and not visited[nx][ny]:
                    queue.append((nx,ny))
                    cost[nx][ny] = cost[x][y] + 1

    return cost

def solve():
    results = []

    # 벽 안부시고 이동해서 cost를 계산해 봄
    cost = bfs(original_graph,(0,0))[ROWS-1][COLS-1]
    if cost!= 0:
        results.append(cost)
    # 벽하나씩 부숴서 각각 cost 구한후 cost 가 0이 아닌 값들중에 최솟값을 정답으로 출력
    for i in range(len(WALLS)):
        wall_x, wall_y = WALLS[i]
        graph_break_one_wall = [item[:] for item in original_graph]
        graph_break_one_wall[wall_x][wall_y] = 0

        cost = (bfs(graph_break_one_wall,(0,0)))
        if cost[ROWS-1][COLS-1] != 0:
            results.append(cost[ROWS-1][COLS-1])

    if results:
        sys_out(min(results)+1)
    else:
        sys_out(-1)

solve()
