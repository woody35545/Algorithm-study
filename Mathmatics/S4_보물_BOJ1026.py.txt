# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# min(S) 를 구하는 프로그램 만들기
# A를 재배열하여 최솟값 나오도록 해야함
# B는 고정값이므로 재배열하면 안됨

import copy


def insertion_sort(_list, type):
    sorted_list = copy.deepcopy(_list)
    for i in range(len(sorted_list)):
        for j in range(i, 0, -1):
            if (type == "inc"):
                if (sorted_list[j - 1] > sorted_list[j]):
                    sorted_list[j - 1], sorted_list[j] = sorted_list[j], sorted_list[j - 1]
            elif (type == "dec"):
                if (sorted_list[j - 1] < sorted_list[j]):
                    sorted_list[j - 1], sorted_list[j] = sorted_list[j], sorted_list[j - 1]
    return sorted_list


def solve():
    N = int(input())
    A = [int(x) for x in input().split(" ")]
    B = [int(x) for x in input().split(" ")]
    # 우선 B를 크기순으로 Sort (내림차순)
    sorted_A_increasing = insertion_sort(A, "inc")
    sorted_B_decreasing = insertion_sort(B, "dec")
    # S 값 계산
    S = 0
    for i in range(len(A)):
        S += sorted_A_increasing[i] * sorted_B_decreasing[i]

    print(S)


solve()
