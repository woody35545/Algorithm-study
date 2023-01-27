import sys

# N = int(sys.stdin.readline().replace("\n", ""))
N = int(input())

for i in range(N):
    # input_line = sys.stdin.readline().replace("\n", "").split(" ")
    input_line = input().split(" ")
    word1 = input_line[0]
    word2 = input_line[1]
    word1_set = set(word1)
    word2_set = set(word2)

    if (len(word1_set ^ word2_set) == 0):
        print(f"{word1} & {word2} are anagrams.")
    else:
        print(f"{word1} & {word2} are NOT anagrams.")
