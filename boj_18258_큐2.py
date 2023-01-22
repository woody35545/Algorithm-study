'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys

from collections import deque
sys_input = lambda: sys.stdin.readline().rstrip()
sys_println = lambda x: sys.stdout.write(str(x)+"\n")
queue = deque([])



def eval(cmd_line) -> None:
    global queue
    cmd_splited = cmd_line.split(" ")

    if cmd_splited[0] == "push":
        queue.append(int(cmd_splited[1]))

    elif cmd_splited[0] == "front":
        if len(queue) == 0:
            sys_println(-1)
        else:
            sys_println(queue[0])

    elif cmd_splited[0] == "back":
        if len(queue) == 0:
            sys_println(-1)
        else:
            sys_println(queue[-1])

    elif cmd_splited[0] == "size":
        sys_println(len(queue))

    elif cmd_splited[0] == "pop":
        if len(queue) == 0:
            sys_println(-1)
        else:
            popped = queue.popleft()
            sys_println(popped)

    elif cmd_splited[0] == "empty":
        if len(queue) == 0:
            sys_println("1")
        else:
            sys_println("0")


N = int(sys_input())
for _ in range(N):
    eval(sys_input())
