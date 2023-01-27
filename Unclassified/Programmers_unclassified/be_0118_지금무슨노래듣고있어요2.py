'''
마지막 노래가 끝나면 첫곡부터 다시 반복되는데 이걸 구현하기 위해 % 연산자로 나머지를 사용하여 노래를 찾도록 하였다. 그런데 만약 나누어 떨어지는 경우(% 연산 결과 == 0)에는 플레이리스트에서 가장
마지막 시간으로 환산해주어야 하는데 이 부분을 고려않았고, 여러가지 예시를 직접 만들어 시도하던 도중 알게되었다. 다음부터 여러 경우의 수가 존재하는 조건분기를 수행할때는 경계값들에 대해서 꼼꼼히 테스트해야겠다 
'''
import sys
music_name = []
questions = []
acc_sum = []

music_info = []

sys_input = lambda: sys.stdin.readline().rstrip()
sys_println = lambda msg: sys.stdout.write(msg + "\n")
sys_print = lambda msg: sys.stdout.write(msg)



def find_music(time):
    if 0 < time <= acc_sum[0]:
        return music_name[0]

    for i in range(0,len(acc_sum)-1):
        if acc_sum[i] < time <= acc_sum[i+1]:

            return music_name[i+1]


N = int(sys_input())
for i in range (N):
    music_name.append(sys_input())

for i in range(N):
    if i == 0:
        acc_sum.append(int(sys_input()))
    else:
        acc_sum.append(acc_sum[i-1] + int(sys_input()))

max_playtime = acc_sum[-1]
M = int(sys_input())

for i in range(M):
    tempQ =int(sys_input())
    if tempQ > max_playtime:
        if tempQ % max_playtime == 0:
            questions.append(max_playtime)
        else:
            questions.append(tempQ % max_playtime)
    else:
        questions.append(tempQ)

for i in range(len(questions)):
    if i == len(questions) -1:
        sys_print(find_music(questions[i]))
    else:
        sys_println(find_music(questions[i]))

