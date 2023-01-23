import sys

sys_input = lambda : sys.stdin.readline().rstrip()
sys_print = lambda msg: sys.stdout.write(str(msg))


input_str = sys_input()
bomb_str = sys_input()

def check_bomb_exists(pStr:str):
    idx = pStr.find(bomb_str)
    if idx == -1:
        return False
    return True

def explode_bomb(pStr:str):
    stack = []
    bomb_ptr = 0
    str_ptr = 0

    while str_ptr != len(pStr):
        #print(f"current string pointer: {str_ptr}")
        if pStr[str_ptr] == bomb_str[0]:
            if len(pStr[str_ptr:]) >= len(bomb_str) and pStr[str_ptr:str_ptr + len(bomb_str)] == bomb_str:
                #print(pStr[str_ptr:str_ptr + len(bomb_str)])
                #print(f"i: {str_ptr} -> ", end=" ")
                str_ptr += len(bomb_str)
                #print(f"{str_ptr}")
                continue
        stack.append(pStr[str_ptr])
        str_ptr += 1

    result = ''.join(map(str, stack))
    return result

def solve():
    str_to_bomb = input_str
    while check_bomb_exists(str_to_bomb):
        str_to_bomb = explode_bomb(str_to_bomb)

    if len(str_to_bomb) > 0:
        sys_print(str_to_bomb)
    else:
        sys_print("FRULA")

solve()
