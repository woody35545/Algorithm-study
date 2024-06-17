"""
문제 출처: https://www.codetree.ai/missions/2/problems/best-place-of-33?&utm_source=clipboard&utm_medium=text
"""

import sys

# variables
N = int(sys.stdin.readline())
MAP = [[0]*N for _ in range(N)]
currentMax = -1

def calc3by3Grid(startX,startY):
    global MAP
    sum = 0

    for i in range(3):
        for j in range(3):
            sum += MAP[startY+i][startX+j]
    return sum

# init input
for i in range(N):
    inputLine = sys.stdin.readline()
    numbers = inputLine.split(" ")
    for j in range(N):
        MAP[i][j] = int(numbers[j])

# traversal
MAX_X_MOVEMENT = N - 3 + 1
MAX_Y_MOVEMENT = N - 3 + 1
curX = 0
curY = 0

for d in range(MAX_Y_MOVEMENT):
    for r in range(MAX_X_MOVEMENT):
        # calc current max
        currentSum = calc3by3Grid(curX,curY)

        if currentSum > currentMax:
            currentMax = currentSum

        # update X position
        curX += 1

    # update Y position
    curY += 1

    # reset X, cause it's next row
    curX = 0

print(currentMax)
