test_graph = [[],
              [2,3],
              [1,4,5],
              [1,4,6],
              [2,3],
              [2,6],
              [3,5]
              ]

def bfs(graph, startVertex):
    visited, queue = [], [startVertex]
    print("* Initial Queue >> " + str(queue) +"\n")
    while queue:

        cur_node = queue.pop(0)  # left pop
        print("[>] pop <Node " + str(cur_node) +">")
        if cur_node not in visited:
            visited.append(cur_node) # if current node's visited state is 'not visited', set 'visited'
            print("[>] set <Node " + str(cur_node) + "> to visited")
            queue.extend(graph[cur_node]) # push current node's adjacent nodes to queue
            print("[>] push <Node " + str(cur_node) + "> 's adjacent nodes " + str(graph[cur_node])+ " to Queue")
        else:
            print("[>] <Node "+ str(cur_node) +"> is already visited!")
        print("---- STATUS ----")
        print("** Popped >> " + str(cur_node))
        print("** Queue >> " + str(queue))
        print("** Visited >> " + str(visited))
        print("")
    return visited

#print(bfs(test_graph,1))


def bfs_with_adjMatrix(graph, startVertex):
    visited, queue = [], [startVertex]
    while queue:
        cur_node = queue.pop(0)  # left pop
        if cur_node not in visited:
            visited.append(cur_node) # if current node's visited state is 'not visited', set 'visited'
            for i in range(len(graph[cur_node])): # current node's adjacent nodes
                if graph[cur_node][i] == 1: # check if it's connected node
                    queue.append(i) # push current node's adjacent nodes to queue
    return visited

  
adj_matrix = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0],
              [0, 1, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 1, 0, 1],
              [0, 0, 1, 1, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 1],
              [0, 0, 0, 1, 0, 1, 0]]

  
print(bfs_with_adjMatrix(adj_matrix,1))
