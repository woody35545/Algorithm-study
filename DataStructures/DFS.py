graph = [[],
         [4,3,2],
         [4,1],
         [4,1],
         [3,2,1]]

def dfs(_graph, _start_node):
    visited, stack = [], []

    # push start node to stack
    stack.append(_start_node)

    while stack:
        current_node = stack.pop()

        # if current node is already visited, end turn and go to first part of while loop
        if current_node in visited:
            continue

        # else current node is not in visited list, add to visited list and check adjacent nodes
        visited.append(current_node)
        for adjacent_node in _graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)

    return visited
  
print(dfs(graph,1))

visited = []
# 재귀함수로 구현한 DFS
def dfs_recursive(_graph, _start_node):
    global visited
    
    # 이미 방문한 노드일 경우 탐색 종료
    if _start_node in visited:
        visited.append(_start_node)
        return

    # visited 처리
    visited.append(_start_node)

    # 인접 노드들에 대해서 Recursive 방식으로 dfs 수행
    for adjacent_node in _graph[_start_node]:
        dfs_recursive(_graph, adjacent_node)
