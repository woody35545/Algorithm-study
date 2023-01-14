from collections import deque
N,M = 0,0
graph = [[0] * (N + 1)]


def bfs(graph, start_vertex:int):
    queue = deque([start_vertex])
    vertex_color = [-1] * (N+1)
    vertex_color[start_vertex] = 0
    visited = [start_vertex]
    while queue:
        for _ in range(len(queue)):
            cur_vertex = queue.popleft()

            for i in range(len(graph[cur_vertex])):
                neighbor_vertex = graph[cur_vertex][i]
                if neighbor_vertex not in visited:
                    queue.append(neighbor_vertex)
                    visited.append(neighbor_vertex)
                    if vertex_color[cur_vertex] == 0:
                        vertex_color[neighbor_vertex] = 1
                    elif vertex_color[cur_vertex] == 1:
                        vertex_color[neighbor_vertex] = 0


        # check if duplicated vertex exists
        for k in range(len(graph[cur_vertex])):
            neighbor_vertex_of_cur = graph[cur_vertex][k]
            #print(f"current_vertex/color: {cur_vertex}/{vertex_color[cur_vertex]}, neighbor/color: {neighbor_vertex_of_cur}/{vertex_color[neighbor_vertex_of_cur]} ")
            if vertex_color[neighbor_vertex_of_cur] != -1 and (vertex_color[cur_vertex] == vertex_color[neighbor_vertex_of_cur]):
                        # Duplicated
                        print("impossible")
                        return False
        #print(" ")

    print("possible")
    return True




def solve():
    global N,M,graph
    N, M = map(int, input().split())
    #print(f"N = {N}")
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)

    bfs(graph,a)
T = int(input())

for _ in range(T):
    solve()
