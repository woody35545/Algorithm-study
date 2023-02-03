import sys
from queue import PriorityQueue
sys_in = sys.stdin.readline
sys_out = sys.stdout.write

N = int(sys_in())
lopes = PriorityQueue()
for i in range(N):
    input_data = int(sys_in())
    lopes.put(input_data)

results = []

while lopes.qsize() > 0:
    old_qsize = lopes.qsize()
    min_lope = lopes.get()
    current_max = min_lope*(old_qsize)

    results.append(current_max)

sys_out(str(max(results)))
