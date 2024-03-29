input(); diff = (list(map(lambda x:abs(320 - x), list(map(int, input().split())))))
print(diff.index(min(diff)) + 1, end ="")


'''
문제 설명
320개
문제
훈련된 초밥 장인이 한 번 초밥을 쥘 때 담는 밥알은 320개라고 알려져 있다.

일식집에서 아르바이트를 하는 준식이는 N 개의 초밥을 열심히 만들어 보았지만 각 초밥에 담긴 밥알의 개수가 제각각이었다. 이 중에서 그나마 밥알의 개수가 320개에 가장 가까운 초밥 하나를 손님에게 내놓으려고 한다. 준식이는 몇 번째 초밥을 내놓아야 할까?

입력
첫째 줄에 초밥의 개수 N (1 ≤ N ≤ 100) 이 주어진다.

둘째 줄에 A[1], A[2], ... , A[N] (1 ≤ A[i] ≤ 1 000) 이 주어진다. i 번째 초밥의 밥알의 개수는 A[i] 개다.

출력
밥알의 개수가 320개에 가장 가까운 초밥은 몇 번째 초밥인지 출력한다. 만약 이러한 초밥이 여러 개 있다면 가장 앞서는 것을 출력한다.

예제 입력 1
3
280 400 330
예제 출력 1
3
예제 입력 2
4
480 310 350 220
예제 출력 2
2
예제 입력 3
2
320 320
예제 출력 3
1
예제 입력 4
3
400 350 290
예제 출력 4
2
예제 입력 5
2
1000 999
예제 출력 5
2
'''
