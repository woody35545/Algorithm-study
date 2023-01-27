# 23.01.26 시간 복잡도 주의하자. elem in list -> 이 방식 사용하면 복잡도가 O(N)이므로 알고리즘 문제 풀이에서는 지양하자

from collections import deque
import sys

sysin = lambda : sys.stdin.readline().rstrip()
sysout = lambda x : sys.stdout.write(str(x)+'\n')

nCity, nRoad, target_dist, start = map(int,input().split())
graph = [[] for _ in range(nCity+1)] # 1 <= city_name <= N

for i in range(nRoad):
    a, b = map(int, sysin().split())
    # directed graph
    graph[a].append(b)

def bfs(start):
    queue = deque([start])
    visited = [False] * (nCity+1)
    #dists = [0] * (nCity+1)
    dist = 0
    res = []
    while queue:

        for _ in range(len(queue)):
            x = queue.popleft()

            if not visited[x]:
                visited[x] = True

                if dist == target_dist:
                    res.append(x)

                #dists[x] = dist

                for city in graph[x]:
                    if not visited[city]:
                        queue.append(city)


        dist += 1

    if res:
        res.sort()
        for i in res:
            sysout(i)
        return res

    else:
        sysout(-1)
        return -1

bfs(start)
