# Not Solved

```python

import sys

sys_in = lambda : sys.stdin.readline().rstrip()
sys_out = lambda x : sys.stdout.write(x)

# N: 사람 수, M: 관계 수
N, M = map(int, sys_in().split(" "))

adj_list_graph = [[] for _ in range(N)]

for i in range(M):
    p, q = map(int, sys_in().split(" "))
    adj_list_graph[p].append(q)
    adj_list_graph[q].append(p)

visited = [False] * N

found = 0


def dfs(current, depth):
    global visited, found

    # print("depth: " + str(depth))

    visited[current] = True

    if depth == 4:
        found = 1
        return

    for j in range(len(adj_list_graph[current])):

        current_neighbor = adj_list_graph[current][j]

        if not visited[current_neighbor]:

            visited[current_neighbor] = True
            # print("call dfs(" + str(current_neighbor) + ", " + str(depth + 1)+ ")")
            dfs(current_neighbor, depth + 1)

            # 초기화
            visited[current_neighbor] = False


for i in range(N):

    if found != 1:
        dfs(i, 0)

sys_out(str(found))

```
