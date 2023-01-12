DP =[]
N = 0
def init_variables():
    global DP,N
    # Reset DP list
    DP = []

    N = int(input())
    DP = [0]*(N+1)
    if N > 3:
        DP[1] = 1
        DP[2] = 2
        DP[3] = 4

def solve():
    global DP
    if N == 1:
        res = 1
        return res
    elif N == 2:
        res = 2
        return res
    elif N == 3:
        res = 4
        return res

    for i in range(4,N+1):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
    return DP[N]

    None

T = int(input())
for i in range(T):
    init_variables()
    answer = solve()
    print(answer)
