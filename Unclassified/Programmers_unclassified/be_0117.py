# Notations
PLAYER = '@'
WALL = '#'
EMPTY = '.'
THORN = '^'

L,R,U,D = (0,-1),(0,1),(-1,0),(1,0)
DIR = {'L':(0,-1), 'R': (0,1), 'U': (-1,0), 'D': (1,0)}

ROW_MAX, COL_MAX =0,0
graph = []
player_position = (-1,-1)
accumulated_demage = 0
walls = []
thorns = []
commands = ""

T = int(input()) # num of testcase

def init_input():
    global graph, ROW_MAX, COL_MAX, commands,accumulated_demage

    # initialize
    walls.clear()
    graph.clear()
    thorns.clear()
    set_player_position((-1,-1))
    accumulated_demage = 0

    ROW_MAX,COL_MAX = map(int,input().split())
    graph = [['.']*COL_MAX for _ in range(ROW_MAX)]

    for i in range (ROW_MAX):
        current_row = list(input())
        for j in range(COL_MAX):
            current_value = current_row[j]

            if current_value == WALL:
                walls.append((i,j))
            if current_value == THORN:
                thorns.append((i,j))
            if current_value == PLAYER:
                set_player_position((i,j))

            graph[i][j] = current_value

    K = int(input())

    commands = input()


def set_player_position(position:tuple):
    global player_position
    player_position = (position[0],position[1])


def movable(next_position: tuple) -> bool:
    next_x, next_y = next_position[0],next_position[1]

    if 0 <= next_x < ROW_MAX and 0 <= next_y < COL_MAX:
        if (next_x, next_y) not in walls:
            return True

    return False


def move(command:str):
    nx, ny = player_position[0] + DIR[command][0], player_position[1] + DIR[command][1]

    if movable((nx,ny)):
        set_player_position((nx, ny))




def print_player_position_and_demage():
    print(str(player_position[0]+1) + " " + str(player_position[1]+1) + " " + str(accumulated_demage))

def solve():
    global answers, accumulated_demage
    init_input()
    for i in range(len(commands)):
        move(commands[i])
        if (player_position[0],player_position[1]) in thorns:
            accumulated_demage += 1

    print_player_position_and_demage()

for _ in range(T):
    solve()
