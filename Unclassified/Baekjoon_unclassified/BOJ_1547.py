T = int(input())
cups = [0, 1, 0, 0]  # 컵은 세개이지만 인덱스를 편하게 다루기 위해 size=4 로 선언


def swap(i, j):
    global cups
    temp = cups[i]
    cups[i] = cups[j]
    cups[j] = temp


for i in range(T):
    a, b = [int(x) for x in input().split(" ")]
    swap(a, b)

for j in range(4):
    if (cups[j] == 1):
        print(j)
