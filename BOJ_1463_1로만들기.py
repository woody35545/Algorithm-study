'''
리스트의 크기가 문제에서 제시한 input으로 정의되고
리스트 값중에 일부를 초기화 하고 시작하려고 할 때는 input 길이를 반드시 체크해서 indexOutRange가 나지 않도록 주의해야한다.
'''
N = int(input())
DP = [0]*(N+1)

if N > 0:
    DP[1] = 0


# bottom - up
def solve(n):
    global DP


    for i in range(2,N+1):
        DP[i] = DP[i-1] + 1 # 1 빼는 연산
        if i%2==0:
            idx = int(i/2)
            DP[i] = min(DP[i], DP[idx] + 1)

        if i%3==0:
            idx = int(i/3)
            DP[i] = min(DP[i], DP[idx] + 1)


    return DP[n]

print(solve(N))
