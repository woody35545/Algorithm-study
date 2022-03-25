dic = {}


def count_plus(_number):
    global dic
    # dictionary에 존재하지 않는 다면 add 하고 value를 1 증가시킴
    # 이미 dictionary에 존재하면 값 하나 증가 시킴
    if not str(_number) in dic:
        dic[str(_number)] = 1
    else:
        dic[str(_number)] = dic[str(_number)] + 1


def solve():
    N = int(input())
    for i in range(N):
        num = int(input())
        count_plus(num)

    #sorted_dic = sorted(dic.items())
    #max_key = max(sorted_dic, key=sorted_dic.get)
    #print(max_key, end="")


solve()
