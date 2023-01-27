for i in range(int(input())):
    _input_tokens = input().split(" ")
    _input_word = _input_tokens[1]
    res = ""

    for j in range(len(_input_word)):
        for k in range(int(_input_tokens[0])):
            res += _input_word[j]

    print(res)
