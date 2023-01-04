'''
개미 탈출 1
문제
준식이는 테슬라 주식을 다량 보유한 서학 개미다. 준식이는 1차원 세상의 왼쪽 끝에 위치해 있고, 1차원 세상의 오른쪽 끝으로 이동해 탈출하려고 한다. 
준식이는 1차원 세상에서 현재 위치한 칸에서 왼쪽 칸이나 오른쪽 칸으로 움직일 수 있다. 준식이가 가는 길에 벽이 있을 수도 있다. 
준식이는 화가 많이 났기 때문에 주먹으로 최대 한 개의 벽을 부수고 지나갈 수 있다.

@.#...O
준식이가 위치한 1차원 세상을 표현한 지도가 주어질 때 준식이는 1차원 세상을 탈출할 수 있을지 구해보자.

입력
첫째 줄에 1차원 세상을 표현한 길이 7짜리 문자열 S 가 주어진다.
문자열의 맨 왼쪽 문자는 언제나 @ 이고, 준식이가 위치한 1차원 세상의 왼쪽 끝을 의미한다.
문자열의 맨 오른쪽 문자는 언제나 알파벳 O 이고, 준식이가 이동하려고하는 1차원 세상의 오른쪽 끝을 의미한다.
나머지 위치의 문자는 . 이거나 # 이다. . 은 빈 칸을 의미한다. 준식이는 빈 칸으로 자유롭게 이동할 수 있다. # 은 벽을 의미한다. 
준식이는 벽이 있는 칸으로 이동할 수 없지만, 최대 한 개의 벽은 부술 수 있다.

출력
준식이가 1차원 세상을 탈출할 수 있다면 HAHA! 를 출력한다. 그렇지 못하다면 HELP! 를 출력한다. 모두 대문자로 출력해야 하는 것에 유의한다.


예제 입력 1
@..#..O
예제 출력 1
HAHA!

예제 입력 2
@#####O
예제 출력 2
HELP!
준식이는 최대 한 개의 벽만 부술 수 있기 때문에 탈출할 수 없다.

예제 입력 3
@.....O
예제 출력 3
HAHA!

'''

def solve():
    world_map = input()
    startPosition = -1
    breakWall = 1

    # find start position
    for i in range(len(world_map)):
        if(world_map[i] == '#'):
            startPosition = i
            break

    # go through with one break wall chance
    for i in range(startPosition,len(world_map)):
        if world_map[i] == '#':
            if breakWall == 0:
                return "HELP!"
            else:
                breakWall-=1
                
    return "HAHA!"

print(solve())
