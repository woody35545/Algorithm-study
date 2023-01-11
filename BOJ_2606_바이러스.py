num_of_computers = int(input())
num_of_relations = int(input())
graph = [[0]*(num_of_computers+1) for _ in range(num_of_computers+1)]

# initialize
for i in range(num_of_relations):
    com1, com2 = map(int, input().split(" "))
    graph[com1][com2] = 1
    graph[com2][com1] = 1

def bfs(graph, start_node):
    num_of_infection = 0

    visited = []
    queue = [start_node]

    while queue:
        cur = queue.pop(0) # left pop for using list like queue
        if cur not in visited:
            visited.append(cur)

            # check neighbors
            for i in range(len(graph[cur])):
                if graph[cur][i] != 0 and i not in visited:
                    queue.append(i)

    return visited

print(len(bfs(graph, 1)[1:]))
