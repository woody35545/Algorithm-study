import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

list_graph = [[] for _ in range(N+1)]
parent = [0]*(N+1)

def find(target):
    if target == parent[target]:
        return target
    else:
        parent[target] = find(parent[target])
        return parent[target]

def union(a,b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa

for i in range(1,N+1):
    input_list = list(map(int, sys.stdin.readline().split(" ")))

    for j in range(len(input_list)):
        if input_list[j] == 1:
            list_graph[i].append(j+1)
            #list_graph[j+1].append(i)

# parent를 자기 자신으로 초기화
for i in range(1, N+1):
    parent[i] = i

# 연결되어 있는 노드끼리 Union 수행
for i in range(1,N+1):
    for neighbor in list_graph[i]:
        union(i, neighbor)

q = list(map(int,sys.stdin.readline().split(" ")))

p = find(q[0])
isConnected = True
for i in range(1,len(q)):
    if p != find(q[i]):
        isConnected = False

print("YES") if isConnected else print("NO")

