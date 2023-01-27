from pprint import pprint
from collections import deque
# Notations
SHEEP = 'o'
WOLF = 'v'
WALL = '#'
EMPTY = '.'


ROWS,COLS = map(int,input().split())
DIRS  = [(-1,0),(1,0),(0,-1),(0,1)]

#graph = [['.']*COLS for _ in range(ROWS)]
graph = []
visited = [[False]*COLS for _ in range(ROWS)]

sections = []

bfs_count = 0

for _ in range(ROWS):
    graph.append(list(input()))

def search_start_position():
    for i in range(ROWS):
        for j in range(COLS):
            if graph[i][j] != WALL and not visited[i][j]:
                return i,j
    return -1,-1


def bfs(start):
    global visited, bfs_count, sections
    queue = deque([start])
    section = []

    while queue:
        #print(queue)
        cur_x,cur_y = queue.popleft()

        if not visited[cur_x][cur_y]:

            visited[cur_x][cur_y] = True
            section.append((cur_x,cur_y))
            #print(f"visited[{cur_x}][{cur_y}] => {visited[cur_x][cur_y]}")
            for dir in DIRS:
                next_x, next_y = cur_x + dir[0], cur_y + dir[1]
                #print(f"next_x:{next_x}, next_y:{next_y}")

                if 0<=next_x<ROWS and 0<=next_y<COLS:
                    if graph[next_x][next_y] != WALL and not visited[next_x][next_y]:
                        queue.append((next_x,next_y))

    bfs_count += 1
    sections.append(section)

#pprint(graph)
start_x, start_y = search_start_position()

while start_x != -1:
    #print(f"bfs({start_x},{start_y})..")
    #pprint(visited)
    bfs((start_x,start_y))
    start_x, start_y = search_start_position()


ts, tw = 0,0

for i in range(len(sections)):
    sheep_count =0
    wolf_count =0
    for j in range(len(sections[i])):

        if graph[sections[i][j][0]][sections[i][j][1]] == SHEEP:
            sheep_count += 1

        elif graph[sections[i][j][0]][sections[i][j][1]] == WOLF:
            wolf_count += 1

    if sheep_count <= wolf_count:
        sheep_count = 0

    else:
        wolf_count = 0

    ts += sheep_count
    tw += wolf_count

print(f"{ts} {tw}", end = " ")
