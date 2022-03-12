T = int(input())
for i in range(T):

    class_score = [int(x) for x in input().split(" ")]
    class_score = class_score[1:len(class_score)]
    class_score.sort()
    Largest_gap = 0
    # show Result
    temp_max = 0

    for j in range(len(class_score) - 1):
         if (temp_max < class_score[j + 1] - class_score[j]):
            temp_max = class_score[j + 1] - class_score[j]
    Largest_gap = temp_max
    print(f"Class {i + 1}")

    print(f"Max {max(class_score)}, Min {min(class_score)}, Largest gap {Largest_gap}")
