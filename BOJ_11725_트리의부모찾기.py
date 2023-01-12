'''
그래프 순회 알고리즘 중 BFS를 이용하여 간단히 해결하였다.
하지만 파이썬 자료구조 별 복잡도에 대해 잘 알지 못해서 시간초과 문제가 발생하였다.
if Elemnt not in List 가 O(N)의 복잡도를 가진다는 것도 처음 알게되었다.(List[Element] 는 O(1)이어서 훨씬 빠르다.
알고리즘 문제풀이에서는 같은 기능을 하는 여러가지 코드들중에서 시간 복잡도를 고려하여 가장 복잡도가 낮은 방법으로 짜도록 연습해야할 필요성을 느꼈다.
'''

from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
#print(graph)
for i in range(N-1):
    #a,b = map(int, input().split(" "))
    a,b = map(int, sys.stdin.readline().rstrip().split(" "))

    #print(a,b)
    graph[a].append(b)
    graph[b].append(a)

#print(graph)

def bfs(graph, start_vertex):
    queue = deque([start_vertex])
    #visited = []
    visited = [False]*(N+1)
    parent = [0]*(N+1)
    while queue:
        cur_vertex = queue.popleft()
        
        #if cur_vertex not in visited:
        if not visited[cur_vertex]:
            #visited.append(cur_vertex)
            visited[cur_vertex] = True
            
            for i in range(len(graph[cur_vertex])):
                child = graph[cur_vertex][i]
                #print(child)

                #if child not in visited:
                if not visited[child]:
                    queue.append(child)
                    parent[child] = cur_vertex
                    #print(parent)
    return parent


parents = bfs(graph,1)
for i in range(2,len(parents)):
    sys.stdout.write(str(parents[i])+"\n")
