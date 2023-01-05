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

    # Determine direction
    if player_pos < exit_pos: # need to go right side
            for i in range(player_pos+1,exit_pos):
                if world_map[i] == wall_char:
                    if break_wall_chance > 0:
                        break_wall_chance -= 1
                    else:
                        return "HELP!"

    else: # need to go left side
        for i in range(1, player_pos - exit_pos - 1):
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
