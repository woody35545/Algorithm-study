"""
R : 한 칸 오른쪽으로
L : 한 칸 왼쪽으로
B : 한 칸 아래로
T : 한 칸 위로
RT : 오른쪽 위 대각선으로
LT : 왼쪽 위 대각선으로
RB : 오른쪽 아래 대각선으로
LB : 왼쪽 아래 대각선으로
"""

x_locations = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
rev_x_locations = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}


class chess_obj:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def show_locations(self):
        print(f"({self.x},{self.y})")

    def move(self, c):
        if (c == "R"):
            if (self.x != 8):
                self.x += 1
        if (c == "L"):
            if (self.x != 1):
                self.x -= 1
        if (c == "B"):
            if (self.y != 1):
                self.y -= 1
        if (c == "T"):
            if (self.y != 8):
                self.y += 1
        if (c == "RT"):
            if (self.x != 8 and self.y != 8):
                self.x += 1
                self.y += 1
        if (c == "LT"):
            if (self.x != 1 and self.y != 8):
                self.x -= 1
                self.y += 1

        if (c == "RB"):
            if (self.x != 8 and self.y != 1):
                self.x += 1
                self.y -= 1
        if (c == "LB"):
            if (self.x != 1 and self.y != 1):
                self.x -= 1
                self.y -= 1


def solve():
    # initialize Location of King and Rock
    loc1, loc2, move_count = input().split(" ")

    king = chess_obj(int(x_locations[loc1[0]]), int(loc1[1]))
    rock = chess_obj(int(x_locations[loc2[0]]), int(loc2[1]))
    # print(f"king: {king.x},{king.y}, rock: {rock.x},{rock.y}")

    for i in range(int(move_count)):

        input_cmd = input()
        if (abs(king.x - rock.x) == 1):
            if (abs(king.y - rock.y) == 0):
                # x 좌표가 인접해있고 y 좌표가 같은 경우
                if (king.x > rock.x):
                    # x 좌표가 king이 더 큰 경우 -> 좌측으로 이동할 때 rock도 옮겨주어야함
                    if (input_cmd == "L"):
                        if (rock.x > 1):
                            king.move(input_cmd)
                            rock.move(input_cmd)
                        else:
                            None
                    else:
                        king.move(input_cmd)
                elif (king.x < rock.x):
                    if (input_cmd == "R"):
                        if (rock.x > 8):
                            king.move(input_cmd)
                            rock.move(input_cmd)
                        else:
                            None
                    else:
                        king.move(input_cmd)
            elif (abs(king.y - rock.y) == 1):
                if (king.y > rock.y):
                    # x좌표와 y좌표가 1씩 차이나는 경우
                    if (king.x > rock.x):
                        # 이때 king.x > king.y 이면 좌하 대각선이동시 rock을 고려해야함
                        if (input_cmd == "LB"):
                            if (rock.x > 1 and rock.y > 1):
                                king.move(input_cmd)
                                rock.move(input_cmd)
                            else:
                                None
                        else:
                            king.move(input_cmd)

                    elif (king.x < rock.x):
                        if (input_cmd == "RB"):
                            if (rock.x < 8 and rock.y > 1):
                                king.move(input_cmd)
                                rock.move(input_cmd)
                            else:
                                None
                        else:
                            king.move(input_cmd)


            elif (king.y < rock.y):
                if (king.x > rock.x):
                    if (input_cmd == "LT"):
                        if (rock.x != 1 and rock.y != 8):
                            king.move(input_cmd)
                            rock.move(input_cmd)
                        else:
                            None
                    else:
                        king.move(input_cmd)

                elif (king.x < rock.x):
                    if (input_cmd == "RT"):
                        if (rock.x != 8 and rock.y != 8):
                            king.move(input_cmd)
                            rock.move(input_cmd)
                        else:
                            None
                    else:
                        king.move(input_cmd)
        elif (king.x == rock.x):
            if (king.y > rock.y):
                if (input_cmd == "B"):
                    if (rock.y != 1):
                        king.move(input_cmd)
                        rock.move(input_cmd)
                    else:
                        None
                else:
                    king.move(input_cmd)

            elif (king.y < rock.y):
                if (input_cmd == "T"):
                    if (rock.y != 8):
                        king.move(input_cmd)
                        rock.move(input_cmd)
                    else:
                        None
                else:
                    king.move(input_cmd)
        else:
            king.move(input_cmd)
        # print(f"king: {king.x},{king.y}, rock: {rock.x},{rock.y}")
    print(rev_x_locations[king.x] + str(king.y))
    print(rev_x_locations[rock.x] + str(rock.y), end="")

while(True):
    solve()
    print()
