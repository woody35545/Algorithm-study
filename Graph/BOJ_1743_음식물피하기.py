from collections import deque
import sys

N,M,K = map(int,sys.stdin.readline().split(" "))
# init input
graph = [[0]*M for _ in range(N)]
DIR = [(0,1), (1,0), (0,-1), (-1,0)]
DIR_X = [0,0,1,-1]
DIR_Y = [-1,1,0,0]
visited = [[False] * M for _ in range(N)]

for i in range(K):
    a,b = map(int,sys.stdin.readline().split(" "))
    graph[a-1][b-1] = 1

def BFS(start:tuple):
    global graph, visited
    queue = deque([start])
    count=0
    while(len(queue)!=0):
        #popped_x, popped_y = queue.pop()
        popped_x, popped_y = queue.popleft()

        visited[popped_x][popped_y] = True
        #print(f"visit {popped_x},{popped_y}")
        count += 1

        for i in range(len(DIR)):
            nx, ny = popped_x + DIR_X[i], popped_y + DIR_Y[i]
            if(nx >= 0 and nx < N and ny >=0 and ny < M and graph[nx][ny] == 1 and not visited[nx][ny]):
                    queue.append((nx,ny))
    return count

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            temp = BFS((i,j))
            if cnt < temp:
                cnt = temp

sys.stdout.write(str(cnt))
