word = input()

bool = True
# 들어온 문자가 짝수일 경우
for i in range(int(len(word) / 2)):
    if (word[i] != word[len(word) - 1 - i]):
        bool = False

if (bool):
    print("1")
else:
    print("0")