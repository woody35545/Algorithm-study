'''
연결 요소의 개수 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
3 초	512 MB	84772	38654	25474	42.608%

문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1 
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1 
2

예제 입력 2 
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
예제 출력 2 
1
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
