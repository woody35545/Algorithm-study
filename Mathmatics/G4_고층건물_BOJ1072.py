N = 0

buildings = [0] * N


# buldings
#   - index: 빌딩 번호
#   - value: 각 빌딩의 높이

def determinant_function(_current_building_number, _target_building_number, x):
    # DET_CA_x: function value(= DET_CA(X))

    # Cx: current_building index
    # Cy: current_building height
    # Ax: a_building index
    # Ay: a_building height

    # x: input variable x

    Cx = _current_building_number
    Cy = buildings[_current_building_number]

    Ax = _target_building_number
    Ay = buildings[_target_building_number]

    DET_CA_x = ((Cy - Ay) / (Cx - Ax)) * (x - Cx) + Cy

    # print(f"DET_CA_x = {DET_CA_x}")

    if (DET_CA_x > buildings[x]):
        return True

    return False


def isViewalbe(_current_building_number, _target_building_number):
    iter = 0  # current와 target 사이에 존재하는 빌딩 수
    if (_current_building_number > _target_building_number):
        iter = _current_building_number - _target_building_number - 1
        for i in range(0, iter):
            # 두 빌딩의 사이에 존재하는 빌딩들 중 하나라도 Determinant를 통과하지 못한다면 False를 리턴
            if (determinant_function(_current_building_number, _target_building_number,
                                     _target_building_number + 1 + i) == False):
                return False

    elif (_current_building_number < _target_building_number):
        iter = _target_building_number - _current_building_number - 1

        for i in range(0, iter):
            if (determinant_function(_current_building_number, _target_building_number,
                                     _current_building_number + 1 + i) == False):
                # 두 빌딩의 사이에 존재하는 빌딩들 중 하나라도 Determinant를 통과하지 못한다면 False를 리턴
                return False

    # Determinant 를 전부 True로 통과한 경우 볼 수 있는 빌딩이므로 True를 리턴
    return True


def get_total_view_count(_current_building_number):
    # total_view_count = 현재 빌딩에서 볼 수 있는 빌딩의 수, return 값
    total_view_count = 0

    # 현재 빌딩 번호에서 특정(target) 빌딩 사이에 방해하는 요소가 있는지 확인하는 function
    # 현재 빌딩 index와 target 빌딩 index 사이의 모든 빌딩에 대하여 -
    # 판별식(Det)를 적용하고, 하나라도 걸리지 않으면 True를 return

    # 우선 현재 건물(current_building) 기준으로 좌우를 비교

    # num_of_buildings_left_side = 현재 지점보다 좌측에 있는 빌딩 수
    # num_of_buildings_right_side = 현재 빌딩보다 우측에 있는 빌딩 수

    num_of_buildings_left_side = _current_building_number  # 좌측 편 빌딩 개수는 현재 빌딩 인덱스와 동일
    num_of_buildings_right_side = N - _current_building_number - 1  # 우측편 빌딩 인덱스는 N-current+1

    # Left Side
    # 현재 빌딩의 번호가 0번이라면 가장 좌측 빌딩이므로 좌측에 대해 수행할 필요가 없음
    if (_current_building_number != 0):
        for i in range(num_of_buildings_left_side):
            if (isViewalbe(_current_building_number, _current_building_number - i - 1)):
                # print(f"[DEBUG] 현재 빌딩: {_current_building_number}, 타겟: {_current_building_number - i - 1}, O")
                total_view_count += 1
            else:
                # print(f"[DEBUG] 현재 빌딩: {_current_building_number}, 타겟: {_current_building_number - i - 1}, X")
                None

    # Right Side
    # 현재 빌딩 번호가 마지막 번호(N-1)라면 가장 우측 빌딩이므로 우측에 대해 수행할 필요가 없음
    if (_current_building_number != N - 1):
        for i in range(num_of_buildings_right_side):
            if (isViewalbe(_current_building_number, _current_building_number + i + 1)):
                # print(f"[DEBUG] 현재 빌딩: {_current_building_number}, 타겟: {_current_building_number + i + 1}, O")

                # print(f"[DEBUG] _current_building_number + i + 1 = { _current_building_number + i + 1}")
                total_view_count += 1
            else:
                # print(f"[DEBUG] 현재 빌딩: {_current_building_number}, 타겟: {_current_building_number + i + 1}, X")
                None
    return total_view_count


def init_input():
    # 문제에서 제시하는 input에 따라서 global variable 초기화
    global N, buildings  # 전역변수 수정을 위해 global variable 임을 명시

    # init N
    N = int(input())

    # N initialize 이후에 다시 buildings 선언
    buildings = [0] * N

    # Building's Height initialize
    buildings = [int(x) for x in input().split(" ")]


def solve():
    buildings_view_count = [0] * N
    # print(f"View Counts of each Buidlings:")

    for i in range(N):
        buildings_view_count[i] = get_total_view_count(i)

    # print(buildings_view_count)
    print(max(buildings_view_count))


def run():
    # N, buildings initialize
    init_input()
    solve()


run()
