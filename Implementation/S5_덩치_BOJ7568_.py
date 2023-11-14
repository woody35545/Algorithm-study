import sys

sys_in = lambda : sys.stdin.readline().rstrip()
sys_out = lambda x : sys.stdout.write(x)

N = int(sys_in())

weight = [0] * N
height = [0] * N

for i in range(N):
    tokens = sys_in().split(" ")

    weight[i] = int(tokens[0])
    height[i] = int(tokens[1])

def getRank(target):
    cnt = 0
    for i in range(0, target):
        if weight[target] < weight[i] and height[target] < height[i]:
           cnt += 1

    if target < N-1:
        for i in range(target + 1, N):
            if weight[target] < weight[i] and height[target] < height[i]:
                cnt += 1

    return cnt+1

for i in range(N):
    sys_out(str(getRank(i)) + " ")
