'''
문제
팬그램(pangram)은 알파벳의 모든 글자를 사용해 만든 문장이다. 주어진 문자열이 팬그램인지 확인해보자.

입력
첫째 줄에 알파벳 소문자로 이루어진 문자열 S (1 ≤ |S| ≤ 100) 가 주어진다. S 는 공백 또는 알파벳 대소문자로 이루어진 문자열이다.

출력
주어진 문자열 S 가 팬그램이라면 YES 를 그렇지 않다면 NO 를 출력한다.

예제 입력 1
The Quick Brown Fox Jumps Over The Lazy Dog
예제 출력 1
YES
예제 입력 2
Bubble sort Quick sort Merge sort prefix sum Binary search Fibonacci Dijkstra
예제 출력 2
NO
예제 입력 3
AbCdEfGhIjKlMnOpQrStUvWxYz
예제 출력 3
YES
'''
import sys

p = lambda x: sys.stdout.write(str(x));l=lambda x : len(x)
s : str = sys.stdin.readline().rstrip();

c_set = set()

[c_set.add(s[i].lower()) if s[i] != " " else None for i in range(l(s))]

p('YES') if l(c_set) == 26 else p('NO')
