# 시간초과로 아직 해결 못함!

# 이분 탐색으로 풀어야 한다고 함.


X = 0
Y = 0
Z = 0


# X = 100판, Y = 60판 이면 Z = (60/100 * 100) %

def calc_Z():
    global X,Y
    return int((Y/X)*100)


def solve():
    global X,Y,Z
    result = 0 # final result

    # Init Input
    X, Y = [int(x) for x in input().split(" ")]
    Z = int((Y/X)*100)
    if(X == Y):
        result = -1
    else:
        while (True):
            result += 1
            # 승리횟수를 하나씩 늘려가면서 Z값을 관찰
            X = X + 1
            Y = Y + 1
            # Z값이 기존 Z값과 달라질때까지 Loop
            if (calc_Z() != Z):
                # 달라질 경우 break
                break

    # Result 출력
    print(f"{result}", end = "")


solve()