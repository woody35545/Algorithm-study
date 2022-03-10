"""
동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.

이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.
"""


# A, B = [int(x) for x in input().split(" ")]
# 1+2+3+4+5+
# 0~n 까지 합: n(n+1)/2

# 1이 커버하는 범위: 1
# 2가 커버하는 범위: 1이 커버하는 범위 + 1 ~ 1+2 = 3 까지
# 3이 커버하는 범위: 2가 커버하는 범위 + 1 ~ 1+2+3 = 6까지
# 4가 커버하는 범위: 3이 커버하는 범위 + 1 ~ 1+2+3+4 = 10까지


def sum(n):
    # n 까지 합 구해주는 메서드
    return n * (n + 1) / 2



A, B = [int(x) for x in input().split(" ")]


def find_segment(_index: int) -> int:
    iter = 0
    while (True):
        # sum(iter-1) + 1 -> segment의 시작 위치

        if (sum(iter - 1) + 1 <= _index and sum(iter) >= _index):
            res_segment = iter
            break
        iter += 1
    location = _index - sum(iter - 1) + 1 - 1
    #print(f"index {_index} 는 segment {res_segment}의 {location} 번째 위치에 있습니다.")
    return res_segment, location


start_segment, start_location = find_segment(A)
end_segment, end_location = find_segment(B)

result = 0
# 우선 경계값들을 더해줌
if (start_segment != end_segment):
    result += (start_segment - start_location + 1) * start_segment + end_location * end_segment
    # 그리고 for문으로 사이값을 더해줌
    for i in range(start_segment + 1, end_segment):
        result += i * i
else:
    result += (end_location - start_location + 1) * start_segment
print(int(result), end = "")
