class Rectangle:
    def __init__(self, lx, ly, rx, ry):
        self.left_x = lx
        self.left_y = ly
        self.right_x = rx
        self.right_y = ry
        self.width = abs(self.right_x - self.left_x)
        self.height = abs(self.right_y - self.left_y)


N = 4  # 문제에서 4개의 케이스로 고정함, 한 케이스에 두 직사각형 비교해서 상태 나타내야함
# 공통부분이 직사각형 = a, 선분 = b, 점 = c, 없음 = d
rec_A = Rectangle()
rec_B = Rectangle()

for i in range(N):
    lx_A, ly_A, rx_A, ry_A, lx_B, ly_B, rx_B, ry_B = [int(x) for x in input().split(" ")]
    rec_A = Rectangle(lx_A, ly_A, rx_A, ry_A)
    rec_B = Rectangle(lx_B, ly_B, rx_B, ry_B)

# 헷갈리지 않도록 A 사각형을 기준으로 판단할거임

# 1. 겹치는 경우인지 판단. -> A의 x 좌표 범위를 공유한다고 했을때 y 좌표도 공유하는 부분이 있으면 겹친거임
