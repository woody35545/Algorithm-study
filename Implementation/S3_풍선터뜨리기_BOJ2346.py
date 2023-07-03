import sys
N = int(sys.stdin.readline())
data = list(map(lambda x: int(x), sys.stdin.readline().split(" ")))
visited = [False]*N
visited_count = 0
start = 0
current, next = -1,-1

while visited_count != N:
    current = next
    if visited_count == 0:
        current = start

    visited[current] = True
    print(current+1, end = " ")

    visited_count += 1

    cnt = data[current]

    next = current

    # set next
    while cnt != 0 and visited_count != N:

        if cnt > 0:
            if not visited[(next + 1) % N]:
                cnt -= 1
            next = (next + 1) % N

        elif cnt < 0:
            if not visited[next-1]:
                cnt += 1
            next = next - 1 if next - 1 >= 0 else next - 1 + N
