from pprint import pprint
width, height = -1,-1
directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)] # Up, Down, Left, Right, Left Up, Left Down, Right Up, Right Down
need_to_find = 0
found = []
dfs_search_count = 0

def search_next_start_node(graph):
    for i in range(height):
        for j in range(width):
            if graph[i][j] == 1 and (i,j) not in found:
                return (i,j)

    return (-1,-1)

def dfs(graph, start_node:tuple):
    global found, dfs_search_count

    stack = [start_node]
    visited = [[False]*width for _ in range(height)]

    while stack:
        current_node = stack.pop()
        if not visited[current_node[0]][current_node[1]]:
            visited[current_node[0]][current_node[1]] = True
            found.append((current_node[0],current_node[1]))

            for i in range(len(directions)):
                next_x = current_node[0] + directions[i][0]
                next_y = current_node[1] + directions[i][1]
                if 0 <= next_x < height and 0 <= next_y < width:
                    if graph[next_x][next_y] != 0 and not visited[next_x][next_y]:
                        stack.append((next_x,next_y))

    dfs_search_count += 1

def solve():
    global need_to_find,found,dfs_search_count
    world_map = []
    need_to_find = 0
    dfs_search_count = 0
    found = []
    for i in range(height):
        list_to_append = list(map(int, input().split(" ")))
        need_to_find += list_to_append.count(1)
        world_map.append(list_to_append)


    while len(found) != need_to_find:
        search_result = search_next_start_node(world_map)
        if search_result != (-1,-1):
            dfs(world_map, search_result)


    print(dfs_search_count)

while(True):
    width, height = map(int, input().split(" "))
    if width == 0 and height == 0:
        break

    solve()


