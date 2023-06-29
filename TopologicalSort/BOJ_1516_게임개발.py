# category: Topologicla Sort
N = int(input())

list_graph = [[] for _ in range(N+1)] # 인접 리스트 그래프
indegree = [0]*(N+1) # 노드의 진입 차수
self_build_time = [0]*(N+1) # 해당 건물만 생산할 때 들어가는 시간
total_build_time = [0]*(N+1) # 해당 건물이 생산되기 위해 필요한 최소 시간

for i in range(1,N+1):
    tokens = list(map(int,input().split(" ")))

    # build time 초기화
    self_build_time[i] = tokens[0]

    # indegree와 list graph 초기화
    if len(tokens) > 2:
        for k in range(1, len(tokens)-1):
            indegree[i] += 1
            list_graph[tokens[k]].append(i)

def topological_sort():
    global indegree, self_build_time, list_graph,total_build_time

    from collections import deque
    q = deque()

    # 진입 차수가 0인 노드를 큐에 추가
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)

    # sort 시작
    while q:
        popped = q.popleft()

        # neighbor 확인
        for neighbor in list_graph[popped]:

            indegree[neighbor] -= 1

            total_build_time[neighbor] \
                = max(total_build_time[neighbor],
                      self_build_time[popped] + total_build_time[popped])

            if indegree[neighbor] == 0:
                q.append(neighbor)

    for i in range(1,N+1):
        total_build_time[i] += self_build_time[i]
        print(str(total_build_time[i]))

topological_sort()
