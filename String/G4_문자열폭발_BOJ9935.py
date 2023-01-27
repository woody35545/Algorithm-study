import sys

sys_input = lambda : sys.stdin.readline().rstrip()
sys_print = lambda msg: sys.stdout.write(str(msg))


input_str = sys_input()
bomb_str = sys_input()

def solve():
    stack = []
    bomb_length = len(bomb_str)

    for i in range(len(input_str)):
        stack.append(input_str[i])
        if ''.join(stack[-bomb_length:]) == bomb_str:
            for _ in range(bomb_length):
                stack.pop()

    if len(stack) == 0:
        return "FRULA"
    return ''.join(stack)

print(solve())
