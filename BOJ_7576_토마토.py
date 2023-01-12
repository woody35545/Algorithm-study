'''
[23.01.12] 
첫번째 시도에서 list.pop(0)이 시간복잡도가 O(N)이어서 시간초과로 틀렸다. list 대신 deque의 popleft를 사용하여(시간복잡도 O(1)) 해결하였다.
두번째 시도에서는 모든 토마토가 익지 못하는 상황에 -1을 출력하도록 문제에서 조건을 주었는데 문제를 제대로 읽지 않아 해당 조건을 고려하지 않아서 틀렸다.
'''

from collections import deque

# variables about input
R, C = -1, -1
graph = []

# notations
RIPE_TOMATO = 1
UNRIPE_TOMATO = 0
EMPTY_SPACE = -1

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def init_input():
    global R, C, graph

    # Reset Graph
    graph = []

    # init map size
    C, R = map(int, input().split(" "))

    # init map
    for i in range(R):
        graph.append(list(map(int, input().split(" "))))


def find_ripe_tomato():
    res = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] == RIPE_TOMATO:
                res.append((i, j))

    return res

def check_all_tomato_ripe():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == UNRIPE_TOMATO:
                return False

    return True


def bfs(_graph, _start_node_list):
    global graph
    visited = [[False] * C for _ in range(R)]
    #queue = []
    queue = deque()
    cost = [[0] * C for _ in range(R)]  # step 당 1 cost 씩 올려서 최소기간을 계산할 때 사용
    cost_max = 0
    # 익은 토마토가 여러개인 경우 시작점이 여러개가 되므로 리스트로 받도록 함
    queue.extend(_start_node_list)

    while queue:
        # 현재 Queue에 있는 노드들의 자식들이 모두 추가되는 것을 한 스텝으로 묶어줌
        for _ in range(len(queue)):

            cx, cy = queue.popleft()

            if not visited[cx][cy]:
                visited[cx][cy] = True

                # check for neighbors
                for dir in directions:
                    nx, ny = cx + dir[0], cy + dir[1]

                    # check it's valid position
                    if 0 <= nx < R and 0 <= ny < C:
                        if graph[nx][ny] != EMPTY_SPACE and graph[nx][ny] != 1 and not visited[nx][ny]:
                            queue.append((nx, ny))
                            # 익은 토마토로 변경
                            graph[nx][ny] = 1
                            cost[nx][ny] = cost[cx][cy] + 1

                            if cost_max < cost[nx][ny]:
                                cost_max = cost[nx][ny]

    return cost, cost_max


def solve():
    init_input()
    start_position = find_ripe_tomato()
    cost, cost_max = bfs(graph, start_position)

    if check_all_tomato_ripe():

        print(cost_max)
    else:
        print(-1)

solve()
