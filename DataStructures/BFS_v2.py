from pprint import pprint
adjacency_matrix_graph = [[1, 1, 0, 0, 0],
                          [0, 1, 1, 0, 0],
                          [0, 1, 1, 1, 0],
                          [0, 0, 0, 1, 1],
                          [0, 0, 0, 0, 1]]

N, M = 5,5
DEBUG_MODE = False
def dprint(msg):
    if DEBUG_MODE:
        print(msg)

def check_valid_pos(x_pos, y_pos):
    if x_pos >= 0 and y_pos >= 0 and x_pos < M and y_pos < N:
        dprint("valid pos: " + str(x_pos) + ", " + str(y_pos))

        return True
    dprint("Not valid pos!: " + str(x_pos) +", " + str(y_pos))
    return False


delta = [(-1,0),(1,0),(0,-1),(0,1)] # up, down, left, right


def bfs(graph, start_node):
    queue = [start_node]
    visited = [[False]*M for _ in range(N)]
    #visited.append(start_node)
    while queue:
        cur  = queue.pop(0)
        # cur(tuple) like (1,2)
        dprint(">> current pop: " + str(cur[0]) + ", " + str(cur[1]))
        if not visited[cur[0]][cur[1]]:
            dprint(str(cur[0]) + ", " + str(cur[1]) + " is not visited")

            visited[cur[0]][cur[1]] = True
            # if cur != start_node:
            #     graph[cur[0]][cur[1]] += 1

            for k in range (len(delta)):
                next_x = cur[0] + delta[k][0]
                next_y = cur[1] + delta[k][1]

                # check next pos valid
                if check_valid_pos(next_x,next_y):
                    if graph[next_x][next_y] != 0 and not visited[next_x][next_y]:
                        #visited[next_x][next_y] = True
                        graph[next_x][next_y] = graph[cur[0]][cur[1]] + 1
                        queue.append((next_x, next_y))
        else:
            dprint(str(cur[0]) + ", " + str(cur[1]) + " is not visited")

    return visited

bfs(adjacency_matrix_graph,(0,0))
pprint(adjacency_matrix_graph)
