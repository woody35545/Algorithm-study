N = int(input())

for i in range(N):
    score_of_O = 0
    total_score = 0
    input_line = input()
    for j in range(len(input_line)):
        if(input_line[j] == "O"):
            score_of_O += 1
            total_score += score_of_O
        else:
            score_of_O = 0
    print(total_score)