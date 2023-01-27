# L 커서 왼쪽으로 한칸 옮김
# D 커서 오른쪽으로 한칸 옮김
# B 커서의 왼쪽문자 삭제
# P $ : $라는 문자를 커서 왼쪽에 추가
import sys

input_str = sys.stdin.readline().strip("\n")
number_of_command = int(sys.stdin.readline().strip("\n"))

cursor_pointer = len(input_str) - 1  # 현재 커서 위치를 나타내는 포인터
current_string = input_str

"""
만약 입럭 문자열이 abc 이면 초기의 커서 포인터는 len(abc)에 위치
"""


def action(_command_tokens):
    # _command_tokens = [ 'P', 'x' ]
    global cursor_pointer, current_string

    if (_command_tokens[0] == "L"):
        if (cursor_pointer != -1):
            cursor_pointer -= 1

    elif (_command_tokens[0] == "D"):
        if (cursor_pointer != len(current_string) - 1):
            cursor_pointer += 1

    elif (_command_tokens[0] == "B"):
        if (cursor_pointer != -1):
            res_string = current_string[0:int(cursor_pointer)] + current_string[
                                                                 int(cursor_pointer) + 1: len(current_string)]
            current_string = res_string
            cursor_pointer -= 1

    elif (_command_tokens[0] == "P"):
        # ab|c -> "x" 추가하면 cursor_pointer = 2 , ㅣ (abc)[0:cursor_pointer] + input_word(=x) + (abc)[cursor_pointer
        word_to_insert = _command_tokens[1]
        # print(f"cursor_pointer = {cursor_pointer}")
        res_string = current_string[0:int(cursor_pointer + 1)] + word_to_insert + current_string[
                                                                                  int(cursor_pointer + 1): len(
                                                                                      current_string)]
        current_string = res_string
        cursor_pointer += 1


def solve():
    for i in range(number_of_command):
        action(sys.stdin.readline().strip("\n").split(" "))

    print(f"{current_string}")


solve()
