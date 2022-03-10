import sys

S = sys.stdin.readline().replace("\n", "")
N = int(sys.stdin.readline().replace("\n", ""))


def F(i):
    temp_str = S[0:i]
    # print(temp_str[-1])
    if (temp_str[-1] != S[-1]):
        return 0  # 끝이 다르면 셀 필요가 없음

    elif (i == len(S)):
        # 문자열 자기 자신을 경우 자기 길이가 곧 최대 공통 접미사
        return len(S)

    else:
        count = 0
        iter = 0
        while (iter < len(temp_str)):

            if (temp_str[-1 - iter] == S[-1 - iter]):
                count += 1
            else:
                break
            iter += 1
        return count


for i in range(N):
    print(F(int(sys.stdin.readline().replace("\n", ""))))
