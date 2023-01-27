import sys

scores = [0] * 8
sorted_scores = [0] * 8

for i in range(8):
    input_int = int(sys.stdin.readline().rstrip())
    scores[i] = input_int
    sorted_scores[i] = input_int

sorted_scores.sort()
index_of_top5 = [0] * 5
size_of_index_of_top5 = 0
total_score = 0
for i in range(5):
    total_score += sorted_scores[len(sorted_scores) - 1 - i]
    for j in range(8):
        if (sorted_scores[len(sorted_scores) - 1 - i] == scores[j]):
            index_of_top5[size_of_index_of_top5] = j + 1
            size_of_index_of_top5 += 1

index_of_top5.sort()

print(total_score)
for i in range(5):
    print(index_of_top5[i], end="")
    if (i != 4):
        print(" ", end="")
