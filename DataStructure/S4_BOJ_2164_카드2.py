from collections import deque

d= deque([i+1 for i in range(int(input()))])

while len(d) > 1:
    d.popleft()
    d.append(d.popleft())

print(d[0])
