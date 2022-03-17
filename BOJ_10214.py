T = int(input())
total_K = 0
total_Y = 0
for i in range(T):
    for j in range(9):
        Y, K = [int(x) for x in input().split(" ")]
        total_Y += Y
        total_K += K

    if (total_Y > total_K):
        print("Yonsei")
    elif (total_Y == total_K):
        print("Draw")
    else:
        print("Korea")
