'''
리포그램
문제
리포그램(lipogram)은 팬그램(pangram)과 반대되는 개념으로, 알파벳의 일부 글자를 사용하지 않고 만든 문장이다. 주어진 문자열이 리포그램인지 확인해보자.

입력
첫째 줄에 알파벳 소문자로 이루어진 문자열 S (1 ≤ |S| ≤ 100) 가 주어진다. S 는 공백 또는 알파벳 대소문자로 이루어진 문자열이다.

출력
주어진 문자열 S 가 리포그램이라면 YES 를 출력하고 두 번째 줄에 사용하지 않은 알파벳을 출력한다. 사용하지 않은 알파벳은 소문자로 출력하며, 알파벳 순서대로 출력한다.

리포그램이 아니라면 NO 를 출력한다.

예제 입력 1
The Quick Brown Fox Jumps Over The Lazy Dog
예제 출력 1
NO
예제 입력 2
Bubble sort Quick sort Merge sort prefix sum Binary search Fibonacci Dijkstra
예제 출력 2
YES
vwz
예제 입력 3
AbCdEfGhIjKlMnOpQrStUvWxYz
예제 출력 3
NO
'''
import sys
p = lambda x: sys.stdout.write(str(x));l=lambda x : len(x)
s : str = sys.stdin.readline().rstrip();

cnt = [0] * 26

# Counting
for i in range(l(s)):
    if s[i].isalpha():
        cnt[ord(s[i].lower()) - ord('a')] += 1

# Print results
p("NO") if 0 not in cnt else p("YES\n")
[p(chr(i+ord('a'))) if cnt[i] == 0 else None for i in range(l(cnt))]
