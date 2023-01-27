import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

print((N - 1) + N * (M - 1))
