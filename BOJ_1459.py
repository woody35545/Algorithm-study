"""
세준이는 학교에서 집으로 가려고 한다. 도시의 크기는 무한대이고, 도시의 세로 도로는 모든 정수 x좌표마다 있고, 가로 도로는 모든 정수 y좌표마다 있다.
세준이는 현재 (0, 0)에 있다. 그리고 (X, Y)에 위치한 집으로 가려고 한다. 세준이가 걸을 수 있는 방법은 두가지 인데,
하나는 도로를 따라서 가로나 세로로 한 블록 움직여서 이번 사거리에서 저 사거리로 움직이는 방법이고, 블록을 대각선으로 가로지르는 방법이 있다.

세준이가 집으로 가는데 걸리는 최소시간을 구하는 프로그램을 작성하시오.
"""

X, Y, W, S = [int(x) for x in input().split(" ")]
# X,Y: 집좌표, W: 한블록 가는 시간, S: 대각선으로 이동할때 시간

# 자신의 X나 Y 좌표가 집의 X 또는 Y 좌표와 둘중에 하나라도 같아질때까지 대각선으로 이동 -> 같아졌다면 직선이동

walk_step = 0  # 직선으로 간 스텝 수
cross_step = 0  # 대각선으로 간 스텝 수

# 주인공 시작 좌표
current_x = 0
current_y = 0

# 집 좌표
home_x = X
home_y = Y

# 주인공은 0,0 에서 시작하므로 대각선 방향이 우상향하는 방향으로 밖에 못감, 즉 x += 1 , y += 1 방향의 대각선만 갈 수 있다는 의미가 됨 (뒤로 가는 대각선은 최단거리가 아니므로 배제)
# 대각선을 한번 움직일때 얻는 거리적 이득을 직선이동으로 얻으려면 2번을 움직여야함. 그런데 직선으로 2번 움직이는 시간비용이 대각선 1번보다 저렴하다면 직선으로 움직이는게 시간적으로 이득임

if( S < 2*W):
    while (True):
        if (current_x == home_x):
            walk_step += home_y - current_y
            break
        elif (current_y == home_y):
            walk_step += home_x - current_x
            break
        # cross step

        current_x += 1
        current_y += 1
        cross_step += 1

else:
    walk_step += X + Y

total_step = walk_step + cross_step
total_time = walk_step * W + cross_step * S
print(f"{total_step} , {walk_step} , {cross_step}")

print(f"{total_time}")
