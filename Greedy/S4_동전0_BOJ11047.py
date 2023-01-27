N,K = map(int, input().split(" "))
coins = [0]*N
for i in range(N):
    coins[i] = int(input())

target_remains = K
count = 0

while target_remains != 0:
    for i in range(len(coins)):
        if target_remains >= coins[len(coins)-1-i]:
            count += int(target_remains/(coins[len(coins)-1-i]))
            target_remains %= (coins[len(coins)-1-i])

print(count)
