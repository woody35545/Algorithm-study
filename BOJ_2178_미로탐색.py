N, M = 0, 0

def check_valid_pos(x_pos, y_pos):
    if 0 <= x_pos < N and 0 <= y_pos < M:
        return True

    return False


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right


def bfs(graph, start_node):
    queue = [start_node]
    visited = [[False] * M for _ in range(N)]
    while queue:

        cur = queue.pop(0)

        if not visited[cur[0]][cur[1]]:
            visited[cur[0]][cur[1]] = True

            for k in range(len(delta)):
                next_x = cur[0] + delta[k][0]
                next_y = cur[1] + delta[k][1]

                # check next pos valid
                if check_valid_pos(next_x, next_y):
                    if graph[next_x][next_y] != 0 and not visited[next_x][next_y]:
                        graph[next_x][next_y] = graph[cur[0]][cur[1]] + 1
                        queue.append((next_x, next_y))
    return visited


N, M = map(int, input().split(" "))
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

bfs(graph, (0, 0))
print(graph[N-1][M-1])
