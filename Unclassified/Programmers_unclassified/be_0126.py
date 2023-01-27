from collections import deque
N = int(input())
buildings = list(map(int, input().split()))

#print(buildings)


def count(opt='left'):

    if opt == 'left':
        deq = deque([buildings[0]])
        for i in range(len(buildings)):
            if deq[-1] < buildings[i]:
                deq.append(buildings[i])
        return len(deq)

    elif opt == 'right':
        deq = deque([buildings[-1]])
        for i in range(len(buildings)):
            if deq[-1] < buildings[len(buildings)-1-i]:
                deq.append(buildings[len(buildings)-1-i])
        return len(deq)

l,r = count('left'), count('right')
print(f'{l} {r}')
