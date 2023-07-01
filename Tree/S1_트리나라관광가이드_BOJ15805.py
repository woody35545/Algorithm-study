import sys
N = int(sys.stdin.readline())
tree = [0] * N
visited = [False] * N
temp = list(map(int, sys.stdin.readline().split(" ")))

total_node_cnt = 0

prev = None

for i in range(len(temp)):
    cur = temp[i]

    if visited[temp[i]]:
        prev = cur
        continue

    if prev == None:
        # 첫번째 방문한 노드가 Root
        tree[cur] = -1
    else:
        tree[cur] = prev

    visited[temp[i]] = True
    total_node_cnt += 1
    prev = cur

print(total_node_cnt)
for i in range(0, total_node_cnt):
    print(tree[i], end=" ")


