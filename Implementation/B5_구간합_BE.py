A = []
def partial_sum(a,b):
    global A
    res = 0
    for i in range(a-1, b):
        res += A[i]
    return res

N, M = map(int,input().split())
A = list(map(int,input().split(" ")))

for _ in range(M):
    L,R = map(int, input().split(" "))
    print(partial_sum(L,R))
