**문제**: https://www.acmicpc.net/problem/3107  
**유형**: `구현`, `문자열`  

# Solved 

```python
# 하나의 토큰에 대해 축약되지 않은 형태 출력
import sys


def getExtended(token):

    if len(token) == 4:
        return token

    extendedToken = token

    current_length = len(token)

    for _ in range(4 - current_length):
        extendedToken = "0" + extendedToken

    return extendedToken


"""
* tokens
 ex)
    25:09:1985:aa:091:4846:374:bb
    => Tokens[0]: 25, Tokens[1]: 09, Tokens[3]:1985 ...
"""

tokens = input().split(":")

# if len(tokens) > 1:
#     if tokens[0] == '' and tokens[1] == '':
#         tokens.pop(0)

emptyCount = 0
for i in range(len(tokens)):
    if tokens[i] == '':
        emptyCount += 1

if emptyCount > 1:
    tokens.remove('')

#print(tokens)

result = [''] * 8

cur = 0
last_index = 0

while(True):

    if cur == len(tokens):
        break

    cur_token = tokens[cur]

    if cur_token == '':
        for i in range(8-len(tokens)+1):
            result[cur + i] = "0000"

        last_index = 8-len(tokens)
        cur += 1

    else:
        result[last_index + cur] = getExtended(cur_token)
        cur += 1


for i in range(8):
    sys.stdout.write(result[i])
    if i < 7:
        sys.stdout.write(":")
```

# 회고
- 제출전에 여러 경계값에 대해서 테스트케이스 만들어서 확인해보자. ex) ::, 1::, ::1, 1:2::3:4 ...  
