import sys
N, M = map(int, input().split(" "))
input = sys.stdin.readline

parent = [0] * (N+1)

def find(target):
    if target == parent[target]:
        return target
    else:
        # 경로 압축
        parent[target] = find(parent[target])
        return parent[target]

def union(a,b):
    # 각 원소의 루트 찾기
    ra = find(a)
    rb = find(b)

    if ra != rb:
        # 동일한 집합이 아닐경우 union 수행
        parent[rb] = parent[ra]

# 초기에는 각 원소 스스로가 루트인 상태
for i in range(N+1):
    parent[i] = i

for i in range(M):
    action, p,q = map(int, input().split(" "))
    if action == 0:
        # 0 인 경우 union(p,q) 수행
        union(p,q)
    elif action == 1:
        # 1 인 경우 같은 집합에 속하는지 판단하여 YES 또는 NO 출력
        rp = find(p)
        rq = find(q)
        if rq == rp:
            print("YES")
        else:
            print("NO")
