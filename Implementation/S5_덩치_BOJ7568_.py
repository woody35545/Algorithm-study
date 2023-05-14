''' 
리스트에서 for문을 돌려 pop 할 경우 인덱스가 건너뛰어져서 일부 값을 순회하지 않고 건너뛰는 문제가 발생한다. 이를 주의하여 pop 해야 한다.
현재 코드는 위를 고려하지 않아서 정상적인 답이 나오지 않는다.(추후 수정 예정)
''' 

N = int(input())
queue = []
current_rank = 1
dict = {} # 등수 기록용
for i in range(N):
    a,b = map(int,input().split(" "))
    queue.append((a,b))
    dict[(a,b)] = 0

queue = sorted(queue, key=lambda x: (x[0],x[1]))
visited_count = 0
while queue:
    #print('a')
    current_max = queue[-1]
    print(current_max)
    print(queue)
    dict[current_max] = current_rank
    res = [len(queue)-1]
    # 첫번째로 비교가 안되는 애들을 찾아야돼 -> 얘네는 같은 랭크야
    for i in range(len(queue)):
        if i >= len(queue):
            break
        if current_max[1] <= queue[i][1]:
            dict[queue[i]] = current_rank
            popped = queue.pop(i)
            print(f"popped: {popped}")

    current_rank += len(res)

print(dict)
