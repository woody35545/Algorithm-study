import sys
from queue import PriorityQueue

sys_in = sys.stdin.readline
sys_out = sys.stdout.write

N = int(sys_in())
pq = PriorityQueue()

for i in range(N):
    pq.put(int(sys_in()))

# initialize
most_smallest_card, second_smallest_card = 0, 0
acc_comparision = 0

# 카드가 다 합쳐져서 하나만 남을때까지 반복
while pq.qsize() > 1:
    most_smallest_card = pq.get()
    second_smallest_card = pq.get()
    merged_card = most_smallest_card + second_smallest_card

    pq.put(merged_card)
    acc_comparision += merged_card

sys_out(str(acc_comparision))
