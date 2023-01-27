import sys

def sys_input(): return sys.stdin.readline().rstrip()
def sys_println(x): return sys.stdout.write(str(x) + "\n")

T = int(sys_input())
for _ in range(T):
    elements = {}
    answer_idx = 0
    N = int(sys_input())

    A = list(map(int, sys_input().split(" ")))

    for e in A:
        if e not in elements:
            elements[e] = 1
        else:
            elements[e] += 1

    for k in elements:
        if elements[k] == 1:
            sys_println(A.index(k) + 1)
