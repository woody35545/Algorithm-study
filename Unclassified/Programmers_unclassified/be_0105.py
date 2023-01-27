# 어디서 틀렸는지 확인해보니 player 위치보다 exit이 낮은 index에 있을 때, 반복문의 변수(i)를 1부터 시작해서 Loop를 통해 wall인지 아닌지 확인하는 방식으로 풀었는데, 
# Range 계산을 잘못해주어서 체크해야할 값 하나를 놓치는 상황이 발생하고 있었다. 반복문 구간을 계산할 때 주의해야겠다.

exit_char = "O"
wall_char = "#"
player_char = "@"

def solve():
    player_pos = -1
    exit_pos = -1

    # N: length of world map
    # M: number of chance to break wall
    world_map_length, break_wall_chance = map(int,input().split(" "))
    world_map = input()


    # First, we need to find player's pos and exit pos
    for i in range(world_map_length):
        cur_char = world_map[i]
        if cur_char == player_char:
            player_pos = i
        elif cur_char == exit_char:
            exit_pos = i

    #print("> Player Pos: " + str(player_pos) + ", Exit Pos: " + str(exit_pos))
    if player_pos == exit_pos:
        return "HAHA!"
    # Determine direction
    if player_pos < exit_pos: # need to go right side
        #print("[#] Go right side")
        for i in range(player_pos+1,exit_pos):
            #print("[##] Player encountered: " + world_map[i])
            if world_map[i] == wall_char:
                if break_wall_chance > 0:
                    break_wall_chance -= 1
                else:
                    return "HELP!"

    else: # need to go left side
        #print("[#] Go left side")
        for i in range(1, player_pos - exit_pos):
            #print("[##] Player encountered: " + world_map[player_pos-i])
            if world_map[player_pos-i] == wall_char:
                if break_wall_chance > 0:
                    break_wall_chance -= 1
                else:
                    return "HELP!"

    # if all above conditions satisfied, it means the player can escape
    return "HAHA!"

T = int(input()) # number of test case
for i in range(T):
    print(solve())
