from collections import deque

graph = []

N,L,R = map(int,input().split(" "))
for _ in range(N):
    graph.append(list(map(int, input().split(" "))))


ROW_MAX, COL_MAX = N,N
visited = [[0]*COL_MAX for _ in range(ROW_MAX)]

DIRECTIONS =  [(1,0),(-1,0),(0,1),(0,-1)]

is_valid = lambda x,y : 0<=x<ROW_MAX and 0<=y<COL_MAX
can_open = lambda x1,y1,x2,y2 : L <= abs(graph[x1][y1]-graph[x2][y2]) <= R

stage_count = 0
def bfs(start_vertex:tuple):
    global graph, visited
    block_elements = deque([]) # 현재 블럭 원소들의 좌표를 저장하기 위한 덱
    queue = deque([start_vertex])
    open_wall_occur = False
    while queue:
        cx,cy = queue.popleft()

        if not visited[cx][cy]:
            visited[cx][cy] = 1
            block_elements.append((cx,cy))

            for k in range(len(DIRECTIONS)):
                nx,ny = cx + DIRECTIONS[k][0], cy+ DIRECTIONS[k][1]

                if is_valid(nx,ny) and can_open(cx,cy,nx,ny) and visited[nx][ny] == 0:
                    open_wall_occur = True
                    queue.append((nx,ny))
    if open_wall_occur:
        # initialize
        current_block_total = 0
        current_block_total_length = len(block_elements)
        
        for i in range(len(block_elements)):
            current_block_total += graph[block_elements[i][0]][block_elements[i][1]]

        new_value = int(current_block_total / current_block_total_length)
        for i in range(len(block_elements)):
            cur_x, cur_y = block_elements[i]
            graph[cur_x][cur_y] = new_value


    return open_wall_occur

def next_stage():
    global stage_count, visited
    visited = [[0] * COL_MAX for _ in range(ROW_MAX)]
    open_wall_occur = False
    while True:
        find_x, find_y = -1,-1
        for i in range(ROW_MAX):
            for j in range(COL_MAX):
                if visited[i][j] == 0:
                    find_x, find_y = i,j
                    open_wall_occur = (bfs((find_x, find_y)) or open_wall_occur)

        else:
            break

    if open_wall_occur:
        stage_count += 1

    return open_wall_occur

def solve():
    global stage_count
    stage_count = 0
    while True:
        open_wall_occur = next_stage()

        if not open_wall_occur:
            break

    print(stage_count)


solve()
