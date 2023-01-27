# Notations
TARGET = 'D' # Destination
PLAYER = 'S' # Player
WATER = '*'
ROCK = 'X'

PLAYER_CANT_MOVE = [ROCK, WATER]
WATER_CANT_EXTEND = [ROCK, TARGET, WATER]
world_map = []
R,C = 0,0

dir = [(0,1),(0,-1),(1,0),(-1,0)]


def extend_water():
    global world_map

    newly_added = []
    for i in range(R):
        for j in range(C):
            if world_map[i][j] == WATER:
                for move in dir:
                    nx = i + move[0]
                    ny = j + move[1]

                # 물을 확장하려는 좌표가 유효한 범위인지 확인하고 물이 확장될 수 있는 영역인지 확인
                    if 0<=nx<R and 0<=ny<C:
                        if world_map[nx][ny] not in WATER_CANT_EXTEND:
                            if (i,j) not in newly_added:
                                world_map[nx][ny] = WATER
                                newly_added.append((nx,ny))


def bfs(graph, start_node:tuple, dest_node):
    queue = [start_node]
    visited = [[False]*C for _ in range(R)]
    visited[start_node[0]][start_node[1]] = True
    cost = [[0]*C for _ in range(R)]

    while queue:

        extend_water() # 물을 확장시켜놓고 시작하면 다음 확장지역에 가지 못하게 하는 조건을 짜기 수월하므로 확장시키고 시작

        for _ in range(len(queue)):
            # 지금 초기화 되어있는 Queue의 원소들을 모두 처리한게 한 라운드로 해야한다.
            cx, cy = queue.pop(0)

            for diff in dir:
                nx, ny = cx + diff[0], cy + diff[1]

                # check next position is valid
                if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in PLAYER_CANT_MOVE and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cost[nx][ny] = cost[cx][cy] + 1


    if cost[dest_node[0]][dest_node[1]] == 0:
        print("KAKTUS")
    else:
        print(cost[dest_node[0]][dest_node[1]])

    return cost

# init world map
R, C = map(int, input().split(" "))
for i in range(R):
    world_map.append(list(input()))

for i in range(R):
    for j in range(C):
        if world_map[i][j]==PLAYER:
            start_position = (i,j)
        if world_map[i][j] == TARGET:
            destination_position = (i, j)

# bfs start
cost = bfs(world_map, start_position, destination_position)
