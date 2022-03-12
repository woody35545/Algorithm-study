import sys

"""
정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.

A와 B는 양의 정수이고, A < B를 만족한다.
A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.
"""

size_of_S = int(sys.stdin.readline().rstrip())
S = [int(x) for x in input().split(" ")]
n = int(sys.stdin.readline().rstrip())

S.sort()


# 기본적으로 n이 S에 포함되어 있으면 안됨

def isContain():
    global S, n
    res = False
    for i in range(size_of_S):
        if (S[i] == n):
            res = True

    return res


def find_local_min():
    global n, S
    iter = 0
    if (n != max(S) and n != min(S)):

        while (True):
            if (S[iter] > n):
                local_min = iter - 1
                break
            else:
                iter += 1

    return local_min


def find_local_max():
    global n, S
    iter = 0
    if (n != max(S) and n != min(S)):
        while (True):
            if (S[iter] > n):
                local_max = iter
                break
            else:
                iter += 1

    return S[local_max]


def solve():
    global n, S

    res = 0
    if (isContain()):
        res = 0
    elif (n < min(S)):
        res = (n - 1) * (min(S) - n) + (min(S) - n - 1)
    else:
        # S의 원소 사이에 있다는 의미
        local_min = find_local_min()
        # local_max = find_local_max()
        # print(f"n(={n})은 S의 원소 중 {S[local_min]}과 {S[local_min + 1]} 사이에 있습니다.")
        # res = S[local_min + 1] - S[local_min] - 2
        res = (n - S[local_min] - 1) * (S[local_min + 1] - n) + (S[local_min + 1] - n - 1)
    print(res, end="")


solve()
