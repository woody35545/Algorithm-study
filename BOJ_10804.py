# 카드 개수는 20개이지만 array 인덱스와 카드 값을 맞춰주기 위해 size = 21 로 할당
arr = [0] * 21


def init_arr():
    for i in range(21):
        arr[i] = i


def swap(i, j):
    global arr

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# 1,3
def reverse(i, j):
    # swap 을 이용하여 구간 [i,j] 를 reverse
    for n in range(int((j - i + 1) / 2)):
        # 구간 gap / 2 만큼 iter ( int 로 casting 하여 소숫점 버림 )
        swap(i + n, j - n)


def solve():
    # initialize Array
    init_arr()

    for n in range(10):
        # comamnd 가 10줄로 고정되어 있음
        tokens = [int(x) for x in input().split(" ")]
        i = tokens[0]  # 구간 시작
        j = tokens[1]  # 구간 끝
        reverse(i, j)

    # arr 출력
    for i in range(1, 21):
        print(arr[i], end=" ")

solve()