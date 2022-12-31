def dfs(graph, start_node):
    stack, visited = [start_node], []

    while stack:
        cur_node = stack.pop()
        if cur_node in visited:
            continue

        visited.append(cur_node)

        temp = []
        for adj_node in graph[cur_node]:
            if adj_node not in visited:
                temp.append(adj_node)

        temp.sort(reverse=True)
        stack.extend(temp)

    return visited

N, M = map(int, input().split(" "))

# init graph
# 인접리스트로 그래프 표현
graph = [[] for _ in range (N+1)]
for i in range(M):
    node1, node2 = map(int, input().split(" "))
    # 양방향으로 추가
    graph[node1].append(node2)
    graph[node2].append(node1)

#print(dfs(graph, graph[1][0]))

found_set = set()
try_node = 1
for i in range(1,N+1):
    if len(graph[i]) != 0:
        try_node = i


try_count = 0

while len(found_set) != N:
    # try dfs
    dfs_res_list = dfs(graph,try_node)
    for i in dfs_res_list:
        found_set.add(i)

    # find next try node
    for i in range(1,N+1):
        if i not in found_set:
            try_node = i
    try_count += 1

print(try_count, end = "")
