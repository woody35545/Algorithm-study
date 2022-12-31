
'''
[22.12.31] 알려진 테스트케이스 반례로 테스트해보면 전부 통과하는데 어디서 틀리는 것인지 모르겠음.
'''

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

def bfs(graph, start_node):
    queue, visited = [start_node], [start_node]

    while queue:
        cur_node = queue.pop(0)

        temp = []
        for adj_node in graph[cur_node]:
            if adj_node not in visited:
                temp.append(adj_node)

        temp.sort()
        queue.extend(temp)
        visited.extend(temp)

    return visited

N, M, V = map(int, input().split(" "))
# print(N, M, V)

input_list = [input() for _ in range(M)]
#print(input_list)

graph = [[] for _ in range (N+1)] # there is no node named '0' but, add '0' for alignment
#print(graph)
for i in range(len(input_list)):
    node1, node2 = map(int, input_list[i].split(" "))
    # Considering it's undirected graph
    graph[node1].append(node2)
    graph[node2].append(node1)
#print("graph: ")
#print(graph)
#print(graph)

# solve
dfs_res_list = dfs(graph,V)
for i in range(len(dfs_res_list)):
    if i != (len(dfs_res_list) -1 ):
        print(str(dfs_res_list[i]), end = " ")
    else:
        print(str(dfs_res_list[i]))

bfs_res_list = bfs(graph,V)
for i in range(len(bfs_res_list)):
    if i != (len(bfs_res_list) -1 ):
        print(str(bfs_res_list[i]), end = " ")
    else:
        print(str(bfs_res_list[i]), end = "")
