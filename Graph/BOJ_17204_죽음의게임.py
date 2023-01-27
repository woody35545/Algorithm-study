from collections import deque

N, K = map(int,input().split())

target=K

adj_list = [[] for _ in range (N)]

for i in range(N):
    adj_list[i].append(int(input()))
#print(adj_list)


def bfs(start):
    cnt = 0
    queue = deque([start])
    visited = []

    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            if x not in visited:
                if x == target:
                    return cnt

                visited.append(x)

                for neighbor in adj_list[x]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        cnt += 1

    return -1


print(bfs(0))
