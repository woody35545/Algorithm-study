# 숫자카드가 필요한 개수를 셈
# 6과 9는 같이 셈
# 6과 9를 제외하고 나머지 중 가장 큰 수 만큼 세트 필요
# 6과 9를 합산해서 2로 나눔
import math

count = [0] * 10  # count[7] 은 원래 6 개수를 세는 자리지만, 6과 9의 개수를 합산한 후 2로 나눈 값을 저장할것임. 9를 카운트한 값은 0으로 세팅할 것임

input_str = input()
for i in range(len(input_str)):
    if (int(input_str[i]) == 6 or int(input_str[i]) == 9):
        count[9] += 1
    else:
        count[int(input_str[i])] += 1

count[9] = math.ceil(count[9] / 2)  # 올려주어야 정확히 필요한 세트가 나옴

print(max(count))
