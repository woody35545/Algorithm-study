from collections import deque

N = int(input())

tree = [[] for i in range(N)]
idx_dict = {}
idx_cnt = 0

for i in range(N-1):
    # A는 B의 child
    A, B = input().split(" ")
    # 다중 상속을 지원하지 않는다고 하였으므로 자식의 수는 1보다 클 수 없음
    if B not in idx_dict.keys():
        idx_dict[B] = idx_cnt
        idx_cnt += 1

    if A not in idx_dict.keys():
        idx_dict[A] = idx_cnt
        idx_cnt += 1
    tree[idx_dict[B]].append(A)

P,Q = input().split(" ")

def dfs(start, target):
    queue = deque([start])
    visited = [False] * N
    while queue:
        popped = queue.popleft()
        if popped == target:
            return True

        if visited[idx_dict[popped]]:
            continue

        visited[idx_dict[popped]] = True
        # check neighbor
        for cand in tree[idx_dict[popped]]:
            if not visited[idx_dict[cand]]:
                queue.append(cand)
    return False

if dfs(P,Q) or dfs(Q,P):
    print(1)
else:
    print(0)
