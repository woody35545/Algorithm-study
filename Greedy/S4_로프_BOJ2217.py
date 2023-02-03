import sys
from collections import deque

sys_in = sys.stdin.readline
sys_out = sys.stdout.write

N = int(sys_in())

lopes =[]
for i in range(N):
    lopes.append(int(sys_in()))

lopes.sort()
results = []
lopes = deque(lopes)
#c1,c2 = min(lopes)*N, max(lopes)
#sys_out(str(c1)) if c1 > c2 else sys_out(str(c2))

while len(lopes)>0:
    total_weight = sum(lopes)
    min_lope = min(lopes)
    current_max = min_lope*len(lopes)
    #print(f"전부 사용해서 나눠들 경우 {current_max}만큼의 weight을 들 수 있습니다.")

    results.append(current_max)

    lopes.popleft()

#print(f"최대값: {max(results)}")
sys_out(str(max(results)))
