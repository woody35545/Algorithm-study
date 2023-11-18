# Solved

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

    visited[current] = True

    if depth == 4:
        found = 1
        return

    for j in range(len(adj_list_graph[current])):

        current_neighbor = adj_list_graph[current][j]

        if not visited[current_neighbor]:

            visited[current_neighbor] = True
            dfs(current_neighbor, depth + 1)

            # 초기화
            visited[current_neighbor] = False


for i in range(N):

    if found != 1:
        dfs(i, 0)
        visited[i] = False

sys_out(str(found))

```

# 회고
depth가 4가 나오는 경우가 하나라도 있는지 찾기 위해서 dfs 호출 할 때 반복문을 통해 출발노드를 바꿔가면서 수행해주었는데,  
dfs 수행 이후에 방금 수행했던 출발 노드에 대한 `visited` 값을 초기화해주지 않아서 틀렸었다.  

