'''
문제
현진이는 길거리를 걸을 때 에어팟으로 노래를 듣는다. 현진이는 자신만의 플레이 리스트가 있기 때문에 집을 나설 때 마다 플레이 리스트의 노래를 순서대로 이어서 듣고, 모든 플레이 리스트를 듣고 나서야 에어팟을 벗는다.
현진이의 플레이 리스트는 N 개의 곡으로 이루어져 있다. 각각의 곡의 길이(초)를 B[1], B[2], … , B[N] 이라고 하자. 
현진이는 집을 나선지 1 초가 지난 시점부터 B[1] 초까지 1 번째 노래를 듣고, B[1] + 1 초부터 B[1] + B[2] 초까지 2 번째 노래를 듣는 식으로 나머지 모든 노래를 듣는다.
예를 들어 현진이의 플레이 리스트에 있는 3 개의 곡의 길이가 각각 3, 1, 2 라고 하자. 
현진이가 집을 나선지 1 초부터 3 초까지는 첫 번째 노래를 듣는다. 그리고 4 초부터 4 초까지는 두 번째 노래를 듣고, 5 초부터 6 초까지는 세 번째 노래를 듣고 7 초 부터는 노래를 듣지 않는다.
현진이는 길거리를 걷다가 지금 무슨 노래 듣고 있어요? 라는 질문을 자꾸만 받는다. 친절한 현진이는 그럴 때마다 자신이 듣고 있는 노래의 이름을 알려준다. 
M 개의 질문이 주어질 때, 현진이가 뭐라고 대답할 지 맞춰보자!

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10) 이 주어진다.
둘째 줄부터 N 개의 줄에 A[1], A[2], ... , A[N] 이 주어진다. A[i] (1 ≤ i ≤ N) 은 현진이의 플레이 리스트에서 i 번째 곡의 이름을 의미한다. 
A[i] 는 알파벳 대소문자 혹은 공백으로 이루어진 길이 20 이하의 문자열이다. 노래 이름의 처음이나 끝에 공백이 들어간 경우는 없다.
그 다음 줄부터 N 개의 줄에 B[1], B[2], ... , B[N] 이 주어진다. B[i] (1 ≤ B[i] ≤ 300) 은 현진이의 플레이 리스트에서 i 번째 노래의 길이가 몇 초인지를 의미한다.
그 다음 줄에 정수 M (1 ≤ M ≤ 10) 이 주어진다.
그 다음 줄부터 M 개의 줄에 Q[1], Q[2], ... , Q[M] (1 ≤ Q[i] ≤ 3 000) 이 주어진다. 
현진이는 집을 나선지 Q[i] 초가 지날 때 마다 i 번째 질문을 받는다. Q 는 오름차순으로 정렬되어 있고, 현진이는 노래를 듣고 있지 않을 때 질문을 받지 않는다.

출력
M 개의 줄에 걸쳐서 i 번째 질문에 대한 대답을 출력한다. 즉, 현진이가 집에서 나선지 Q[1], Q[2], ... , Q[M] 초가 지났을 때 현진이가 듣고 있는 노래의 제목을 한 줄에 하나씩 출력한다.

예제 입력 1
5
Hype Boy
LOVE DIVE
Nxde
ANTIFRAGILE
Shut Down
180
178
179
185
176
10
1
180
181
358
359
537
538
722
723
898
예제 출력 1
Hype Boy
Hype Boy
LOVE DIVE
LOVE DIVE
Nxde
Nxde
ANTIFRAGILE
ANTIFRAGILE
Shut Down
Shut Down
'''
music_name = []
music_playtime = []
questions = []

def get_partial_sum():
    partial_sum = [0]*len(music_playtime)
    for i in range(len(music_playtime)):
        if i == 0:
            partial_sum[i] = music_playtime[i]
            continue

        partial_sum[i] = music_playtime[i] + partial_sum[i-1]

    return partial_sum

def solve():
    partial_sum = get_partial_sum()

    for i in range(len(questions)):
        if questions[i] <= partial_sum[0]:
            print(music_name[0])
            continue
        if questions[i] > partial_sum[len(partial_sum)-1]:
            print(music_name[-1])
            continue
        for j in range(len(partial_sum)-1):
            if partial_sum[j] < questions[i] <= partial_sum[j+1]:
                print(music_name[j+1])



    return True


N = int(input())
for i in range (N):
    music_name.append(input())

for i in range(N):
    music_playtime.append(int(input()))

M = int(input())

for i in range(M):
    questions.append(int(input()))



solve()
