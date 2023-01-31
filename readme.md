## To Do

|Planning Date|Title|Link|Status|
|:---:|:---:|:---:|:---:|
| 2023.01.09 | **BOJ_4963_섬의_개수** | https://www.acmicpc.net/problem/4963 | Done |
| 2023.01.13 | **BOJ_16234_인구이동** | https://www.acmicpc.net/problem/16234 | Done|
| 2023.01.15 | **BOJ_2357_최솟값과 최댓값** | https://www.acmicpc.net/problem/2357 | | 
| 2023.01.16 | **BOJ_14226_이모티콘** | https://www.acmicpc.net/problem/14226 |  |  
| 2023.01.16 | **BOJ_1890_점프** | https://www.acmicpc.net/problem/1890 | 
| 2023.01.23 | **BOJ_9935_폭발문자열** | https://www.acmicpc.net/problem/9935 |
| 2023.01.25 | **BOJ_2206_벽 부수고 이동하기** | https://www.acmicpc.net/problem/2206| Time Out
| 2023.01.26 | **BOJ_2638_치즈** | https://www.acmicpc.net/problem/2638|
| 2023.01.28 | **BOJ_14502_연구소** | https://www.acmicpc.net/problem/14502|


## Today I Tried or Solved
|Date|Title|Code|Description|
|:---:|:---:|:---:|:---:|
| 2023.01.30 | [**G4_최단경로찾기_BOJ1753**](https://www.acmicpc.net/problem/4963)| [Link](https://github.com/woody35545/Algorithm/blob/master/Dijkstra/G4_%EC%B5%9C%EB%8B%A8%EA%B2%BD%EB%A1%9C_BOJ1753.py) |Python3는 통과하는데 Pypy로는 왜 시간초과가 날까..? |
| 2023.01.31 | [**S1_효율적인해킹_BOJ1325**](https://www.acmicpc.net/problem/1325) | - | Time Out
## Review
- 2023.01.12 - **BOJ_11725_트리의부모찾기**
  - **`if current_vertex not in visited` 와 `if not visted[current_vertex]` -> 동일한 기능이지만 시간복잡도 차이 발생.**  
    `if element in list` 방식의 시간복잡도가 높은편
    - [참고]  
       파이썬 자료형 별 시간복잡도: https://wayhome25.github.io/python/2017/06/14/time-complexity/    
  

  
  - **`input()`, `print()` -> `sys.stidn.readline()`, `sys.stdout.write()` 를 사용하면 시간복잡도 줄어듦**  
      - [참고]   
        https://urakasumi.tistory.com/m/273
