# T
# x1, y1, r1, x2, y2, r2

def distance(a: tuple, b: tuple):
    # e.g) a = (1,2) b = (3,2)
    distance = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (1 / 2)
    # print(distance)
    return distance


def solve():
    T = int(input())
    result_list = [0] * T

    for i in range(0, T):
        result = 0  # result 값 초기화
        x1, y1, r1, x2, y2, r2 = [int(x) for x in input().split(" ")]
        # 반지름이 더 큰 점을 A로 설정
        if (r1 > r2):
            dot_a = (x1, y1)  # A_r = r1
            dot_b = (x2, y2)  # B_r = r2
        else:
            dot_a = (x2, y2)
            dot_b = (x1, y1)
            r1, r2 = r2, r1
            # 가능한 위치 갯수 판단.
            ## A와 B 사이의 거리가 r1+r2 보다 클 경우 -> 교점 없음
        if ((distance(dot_a, dot_b) == 0) and (r1 == r2)):
            result = -1
        elif (distance(dot_a, dot_b) > r1 + r2):
            result = 0
        elif (distance(dot_a, dot_b) == r1 + r2):
            result = 1
        elif (distance(dot_a, dot_b) < r1 + r2):
            if (distance(dot_a, dot_b) < r1 - r2):
                result = 0
            elif (distance(dot_a, dot_b) == r1 - r2):
                result = 1
            elif (distance(dot_a, dot_b) > r1 - r2):
                result = 2
        result_list[i] = result

    for i in range(len(result_list)):
        print(str(result_list[i]), end="")
        if (i != len(result_list) - 1):
            print("")


solve()
