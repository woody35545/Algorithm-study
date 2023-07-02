import sys
from collections import deque

N, M, START = map(int, sys.stdin.readline().split(" "))

# list graph
G = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    p,q = map(int, sys.stdin.readline().split(" "))
    G[p].append(q)



for i in range(len(G)):
    G[i].sort()
    print(G[i])

queue = deque([START])
visited_cnt = 1

while queue:
    popped = queue.popleft()

    if visited[popped] > 0:
        continue
    visited[popped] = visited_cnt
    visited_cnt +=1

    # check neighbor
    for neighbor in G[popped]:
        if visited[neighbor] == 0:
            queue.append(neighbor)

for i in range(1, N+1):
    sys.stdout.write(str(visited[i]) + "\n")
