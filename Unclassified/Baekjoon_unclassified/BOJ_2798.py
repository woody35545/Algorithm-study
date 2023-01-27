N, M = [int(x) for x in input().split(" ")]
cards = [int(x) for x in input().split(" ")]

temp_max = 0
for i in range(N):
    for j in range(i + 1, N ):
        for k in range(j + 1, N):
            if(temp_max < cards[i] + cards[j] + cards[k]):
                if(cards[i] + cards[j] + cards[k] <= M ):
                     temp_max = cards[i] + cards[j] + cards[k]

print(temp_max)