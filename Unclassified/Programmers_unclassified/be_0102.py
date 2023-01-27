N = int(input())
M = list(map(int, input().split(" ")))
Q = int(input())


def sum(_list, _range1, _range2):
    res = 0
    for i in range(_range1-1, _range2):
        res += _list[i]
    return res


for i in range (Q):
    a, b = map(int,input().split(" "))
    print(sum(M,a,b))
