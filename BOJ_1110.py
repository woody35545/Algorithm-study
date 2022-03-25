def init_input():
    input_str = input()
    if (len(input_str) == 1):
        input_str = "0" + input_str
    return input_str


def solve():
    input_str = init_input()
    count = 0  # 사이클을 세기위한 변수 선언
    current_str = input_str

    while True:
        operate_res = str(int(current_str[0]) + int(current_str[1]))
        # Update Current String
        current_str = str(current_str[1]) + str(operate_res[len(operate_res) - 1])

        count += 1

        if current_str == input_str:
            break

    print(count, end="")


solve()
