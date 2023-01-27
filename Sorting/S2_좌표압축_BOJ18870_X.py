"""
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
"""

# [!] 2020.03.10: 시간초과로 다시 풀어야 함
# 오름차순으로 Sorting 하면 자신의 Index가 자기보다 작은 수의 갯수가 됨 -> 이때 동일한 숫자의 경우 예외가 발생하므로 따로 조치해주어야함

N = int(input())
input_tokens = input().split(" ")
X_list = [0] * N
for i in range(N):
    X_list[i] = int(input_tokens[i])

X_set = set(X_list)
X_list2 = list(X_set)
X_list2.sort()




for i in range(N):
    print(X_list2.index(X_list[i]), end = "")

    if (i != N-1):
        print(" " , end = "")