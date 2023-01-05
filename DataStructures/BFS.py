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

print(bfs(test_graph,1))
