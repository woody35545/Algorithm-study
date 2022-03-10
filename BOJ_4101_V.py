while (True):
    A, B = [int(x) for x in input().split(" ")]
    if (A == 0 and B == 0):
        break
    else:
        if (A > B):
            print("Yes")
        else:
            print("No")
