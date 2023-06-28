n, m = map(int, input().split(" "))
res = []

def dfs(l):
    # m개를 골랐다면 출력
    if len(l) == m:
        print(*l)
        return

    # 1부터 n까지 수를 모두 시도
    for cand in range(1,n+1):
        if cand not in l:
            # cand를 선택
            l.append(cand)
            # 더 깊이 탐색을 진행
            dfs(l)
            # 탐색 후 cand 선택을 해제
            l.pop()

dfs(res)
