scores = { 'A+':4.5, 'A0':4, 'B+':3.5, 'B0':3, 'C+':2.5, 'C0':2, 'D+':1.5, 'D0':1, 'F':0 }

score_sum = 0
count = 0
for _ in range(20):
    input_tokens = input().split(" ")

    if input_tokens[2] != 'P':
        grade = float(input_tokens[1])
        score = scores[input_tokens[2]]

        score_sum += grade*score
        count += grade


print(round(score_sum/count,6))
