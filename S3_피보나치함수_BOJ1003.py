import sys
zero_cnt = [1,0,1]
one_cnt = [0,1,1]

def fibo(n):
    if n >= len(zero_cnt):
        for i in range(len(zero_cnt),n+1):
            zero_cnt.append(zero_cnt[i-1] + zero_cnt[i-2])
            one_cnt.append(one_cnt[i-1] + one_cnt[i-2])

    print(str(zero_cnt[n]) + " " + str(one_cnt[n]))

T = int(sys.stdin.readline())

for i in range(T):
    fibo(int(sys.stdin.readline()))

