A = int(input())
B = int(input())
C = int(input())

D = A * B * C
count = [0] * 10
for i in range(len(str(D))):
    if (str(D)[i] == "0"):
        count[0] += 1
    elif (str(D)[i] == "1"):
        count[1] += 1
    elif (str(D)[i] == "2"):
        count[2] += 1
    elif (str(D)[i] == "3"):
        count[3] += 1
    elif (str(D)[i] == "4"):
        count[4] += 1
    elif (str(D)[i] == "5"):
        count[5] += 1
    elif (str(D)[i] == "6"):
        count[6] += 1
    elif (str(D)[i] == "7"):
        count[7] += 1
    elif (str(D)[i] == "8"):
        count[8] += 1
    else:
        count[9] += 1

for i in range(10):
    print(count[i])
