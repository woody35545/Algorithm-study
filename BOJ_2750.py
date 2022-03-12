import sys
N = int(sys.stdin.readline().replace("\n", ""))
data_list = [0] * N
for i in range(N):
    data_list[i] = int(input())

data_list.sort()
for i in range(N):
    print(int(data_list[i]))
    