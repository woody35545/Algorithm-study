**문제**: https://www.acmicpc.net/problem/5430  
**유형**: `구현`, `자료 구조`, `문자열`, `파싱`, `덱`  

# Solved
```python
import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):

    COMMANDS = sys.stdin.readline().rstrip()
    ARR_LEGNTH = int(sys.stdin.readline().rstrip())
    ARR = deque([])
    # 배열이 뒤집어진 상태인지 확인하기 위한 flag
    reverse = False
    error = False

    tmp1 = sys.stdin.readline().rstrip() # '[1,2,3,4]' -> String
    tmp2 = tmp1[1:len(tmp1)-1].split(",") # ['1','2','3','4'] -> List

    for i in range(len(tmp2)):
        if tmp2[i] != '':
            ARR.append(tmp2[i])

    for i in range(len(COMMANDS)):
        if COMMANDS[i] == 'R':
            if reverse == True:
                reverse = False

            elif reverse == False:
                reverse = True

        elif COMMANDS[i] == 'D':
            if len(ARR) == 0:
                # 배열이 비어있는데 D를 사용한 경우에는 에러 발생
                error = True

            else:
                if reverse:
                    ARR.pop()
                else:
                    ARR.popleft()

    if not error:
        if len(ARR) == 0:
            print("[]")

        for i in range(len(ARR)):
            if i == 0:
                sys.stdout.write("[")
            if not reverse:
                sys.stdout.write(str(ARR[i]))
            else:
                sys.stdout.write(str(ARR[len(ARR)-1-i]))

            if i != len(ARR) - 1:
                sys.stdout.write(",")
            else:
                sys.stdout.write("]\n")
    else:
        print("error")
```
