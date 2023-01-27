'''
monster를 마주첬을 경우 싸움에서 이기면 통과하도록 조건식을 짜두고 어디가 잘못되었는지 한참을 찾았다. 
몬스터와 싸운 이후에도 벽이 존재하므로 탈출구가 나올때까지 계속 체크해야되는데 바로 싸움에서 이기면 바로 통과할 수 있다고 생각한 것이 문제였다 .
'''


'''
문제 설명
개미 탈출 4
문제
준식이는 길이가 N 인 1차원 세상의 어딘가에 위치해 있고, 1차원 세상의 어딘가에 위치한 탈출구로 이동하려고 한다. 준식이는 1차원 세상에서 현재 위치한 칸에서 왼쪽 칸이나 오른쪽 칸으로 움직일 수 있다. 
준식이가 가는 길에 벽이 있을 수도 있다. 준식이는 화가 많이 났기 때문에 주먹으로 최대 M 개의 벽을 부수고 지나갈 수 있다.
그런데 어느 날, 1차원 세상에 몬스터가 한 마리 떨어졌다. 준식이가 몬스터가 있는 칸으로 이동하기 위해서는 그 칸에 있는 몬스터와 싸워서 이겨야 한다.
현재 준식이의 공격력을 ATK_J , 체력을 HP_J 라고 하고, 몬스터의 공격력을 ATK_M, 체력을 HP_M 라고 하자. 준식이가 몬스터가 있는 칸으로 이동하면 전투가 시작되고, 전투는 다음과 같이 진행된다.

준식이의 현재 공격력 ATK_J 만큼 몬스터의 현재 체력 HP_M 를 깎는다.
몬스터의 체력이 0 이하이면 몬스터는 사라지고 준식이가 전투에서 이기게 된다.
몬스터의 공격력 ATK_M 만큼 준식이의 현재 체력 HP_J 를 깎는다.
준식이의 체력이 0 이하이면 준식이는 사라지고 몬스터가 전투에서 이기게 된다.
다시 1부터 진행한다.
준식이가 위치한 1차원 세상을 표현한 지도가 주어질 때 준식이는 1차원 세상을 탈출할 수 있을지 구해보자.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스의 첫째 줄에 1차원 세상의 길이 N (3 ≤ N ≤ 8) 와 준식이가 벽을 부술 수 있는 최대 횟수 M (0 ≤ M ≤ N) 가 주어진다.
둘째 줄에 1차원 세상을 표현한 길이 N 짜리 문자열 S 가 주어진다.
문자열에서 @ 는 단 한 번 등장하며, 준식이를 의미한다.
문자열에서 알파벳 대문자 O 는 한 번 이상 등장하며, 준식이가 이동하려는 탈출구를 의미한다.
문자열에서 & 는 단 한 번 등장하며, 몬스터를 의미한다.
나머지 위치의 문자는 . 이거나 # 이다. . 은 빈 칸을 의미한다. 준식이는 빈 칸으로 자유롭게 이동할 수 있다. # 은 벽을 의미한다. 
준식이는 벽이 있는 칸으로 이동할 수 없지만, 최대 M 개의 벽은 부술 수 있다.
셋째 줄에 초기 준식이의 공격력 ATK_J (1 ≤ ATK_J ≤ 100) 와 체력 HP_J (1 ≤ HP_J ≤ 100) 가 주어진다.
넷째 줄에 초기 몬스터의 공격력 ATK_M (1 ≤ ATK_M ≤ 100) 와 체력 HP_M (1 ≤ HP_M ≤ 100) 이 주어진다.

출력
각 테스트 케이스마다 준식이가 1차원 세상을 탈출할 수 있다면 HAHA! 를 출력한다. 그렇지 못하다면 HELP! 를 출력한다. 모두 대문자로 출력해야 하는 것에 유의한다.

예제 입력 1
4
8 1
O&#@##.O
10 10
100 11
3 0
@&O
1 1
1 1
5 0
O#@&O
2 49
1 100
8 3
O#@###&O
1 1
100 100

예제 출력 1
HELP!
HAHA!
HELP!
HAHA!
'''

PLAYER = '@'
EXIT = 'O'
MONSTER = '&'
WALL = '#'

world_map = []
player_start_pos = 0
break_wall_chance = 0
ATK_P, HP_P,ATK_M, HP_M = 0,0,0,0

def init_input():
    global world_map, player_start_pos, break_wall_chance, ATK_P, HP_P, ATK_M, HP_M

    world_length, break_wall_chance = map(int, input().rstrip().split(" "))
    world_map = input().rstrip()

    # Player Attack, Hp
    ATK_P, HP_P = map(int, input().rstrip().split(" "))

    # Monster's Attack, Hp
    ATK_M, HP_M = map(int, input().rstrip().split(" "))

    # init positions
    player_start_pos = world_map.find(PLAYER)



def fight():
    global ATK_P, HP_P, ATK_M, HP_M
    # if Player win return true
    while(True):
        # player attacks monster first
        HP_M -= ATK_P
        if HP_M <= 0:
            return True

        # monster attacks player
        HP_P -= ATK_M
        if HP_P <= 0:
            return False

def left_search():
    left_map = world_map[:player_start_pos]
    left_search_break_wall_chance = break_wall_chance

    for i in range(len(left_map)):
        cur = len(left_map)-1-i

        if left_map[cur] == WALL:
            if left_search_break_wall_chance > 0:
                left_search_break_wall_chance -= 1
            else:
                return False

        elif left_map[cur] == MONSTER:
            if not fight():
                return False

        elif left_map[cur] == EXIT:
            return True

    return False

def right_search():
    right_map = world_map[player_start_pos+1:]
    right_search_break_wall_chance = break_wall_chance
    for i in range(len(right_map)):
        if right_map[i] == WALL:
            if right_search_break_wall_chance > 0:
                right_search_break_wall_chance -= 1
            else:
                return False

        elif right_map[i] == MONSTER:
            if not fight():
                return False

        elif right_map[i] == EXIT:
            return True

    return False


def solve():
    init_input()
    res_left_search = left_search()
    res_right_search = right_search()


    if res_left_search or res_right_search:
        print("HAHA!")
    else:
        print("HELP!")

T = int(input())
for i in range(T):
    solve()
