''' 
23.02.06 - 확실히 파이썬이 자바에 비해서 같은 문제를 풀어도 직관적으로 생각을 구현할 수 있어 알고리즘 풀이용으로는 더 유리한 부분이 있는 것 같다.
'''

int(input())
print(list(map(int, input().split(" "))).count(int(input())), end = "")
