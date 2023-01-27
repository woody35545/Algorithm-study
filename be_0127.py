import sys

def r(): return sys.stdin.readline()
def p(x): return sys.stdout.write(str(x))

N = int(r())
a, b, c, d = map(lambda x: int(x) - 1, r().split())

for i in range(N):
    for j in range(N):
        p('.') if min(a, c) <= i <= max(a, c) and min(b, d) <= j <= max(b, d) else p('*')
    p("\n") if i != N - 1 else None
