# Notations
PLAYER = '@'
WALL = '#'
EMPTY = '.'

L,R,U,D = (0,-1),(0,1),(-1,0),(1,0)


ROW_MAX, COL_MAX =0,0
graph = []
player_position = (-1,-1)
walls = []
commands = ""


T = int(input()) # num of testcase

def init_input():
    global graph, ROW_MAX, COL_MAX, commands

    # initialize
    walls.clear()
    graph.clear()
    set_player_position((-1,-1))


    ROW_MAX,COL_MAX = map(int,input().split())
    graph = [['.']*COL_MAX for _ in range(ROW_MAX)]

    for i in range (ROW_MAX):
        current_row = list(input())
        for j in range(COL_MAX):
            current_value = current_row[j]

            if current_value == WALL:
                walls.append((i,j))
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
    #ext_x, next_y = -1,-1
    if command == 'L':
        next_x, next_y= player_position[0] + L[0], player_position[1] + L[1]
    elif command == 'R':
        next_x, next_y= player_position[0] + R[0], player_position[1] + R[1]
    elif command == 'U':
        next_x, next_y= player_position[0] + U[0], player_position[1] + U[1]
    elif command == 'D':
        next_x, next_y= player_position[0] + D[0], player_position[1] + D[1]

    if movable((next_x,next_y)):
        set_player_position((next_x, next_y))


def print_player_position():
    print(player_position[0]+1,player_position[1]+1)

def solve():
    global answers
    init_input()
    for i in range(len(commands)):
        move(commands[i])

    print_player_position()

for _ in range(T):
    solve()
