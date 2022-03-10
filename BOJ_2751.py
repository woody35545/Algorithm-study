import sys
N = int(sys.stdin.readline())
data = [0] * N
for i in range(N):
    data[i] = int(sys.stdin.readline())

data.sort()
for i in range(N):
    print(data[i])