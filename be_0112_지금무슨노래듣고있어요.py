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
