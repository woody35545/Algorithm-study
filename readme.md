## To Do

|Planning Date|Title|Link|Status|
|:---:|:---:|:---:|:---:|
| 2023.01.09 | **BOJ_4963_섬의_개수** | https://www.acmicpc.net/problem/4963 | Done |
| 2023.01.13 | **BOJ_16234_인구이동** | https://www.acmicpc.net/problem/16234 | Done|
| 2023.01.15 | **BOJ_2357_최솟값과 최댓값** | https://www.acmicpc.net/problem/2357 | - | 
| 2023.01.16 | **BOJ_14226_이모티콘** | https://www.acmicpc.net/problem/14226 | - |  
| 2023.01.16 | **BOJ_1890_점프** | https://www.acmicpc.net/problem/1890 | -
| 2023.01.23 | **BOJ_9935_폭발문자열** | https://www.acmicpc.net/problem/9935 |
| 2023.01.25 | **BOJ_2206_벽 부수고 이동하기** | https://www.acmicpc.net/problem/2206| [!] Time |
| 2023.01.26 | **BOJ_2638_치즈** | https://www.acmicpc.net/problem/2638| - |
| 2023.01.28 | **BOJ_14502_연구소** | https://www.acmicpc.net/problem/14502| - |
| 2023.05.13 | **BOJ_1743_음식물피하기** | https://www.acmicpc.net/problem/1743 | [!] Memory |  
| 2023.11.22 | **G3_개미굴_BOJ14725** | https://www.acmicpc.net/problem/14725 | [!] Fail |
| 2023.11.22 | **G3_디스크트리_BOJ7432** | https://www.acmicpc.net/problem/7432 | done |
| 2023.11.22 | **G3_트리색칠하기_BOJ24230** | https://www.acmicpc.net/problem/24230| |
| 2023.11.23 | **P3_전설_BOJ19585** | https://www.acmicpc.net/problem/19585 | | 
| 2023.11.23 | **G5_서울의지하철_BOJ16166**| https://www.acmicpc.net/problem/16166 | |

## Today I Tried or Solved
|Date|Title|Code|Description|
|:---:|:---:|:---:|:---:|
| 2023.01.30 | [**G4_최단경로찾기_BOJ1753**](https://www.acmicpc.net/problem/4963)| [Link](https://github.com/woody35545/Algorithm/blob/master/Dijkstra/G4_%EC%B5%9C%EB%8B%A8%EA%B2%BD%EB%A1%9C_BOJ1753.py) |Python3는 통과하는데 Pypy로는 왜 시간초과가 날까..? 
| 2023.01.31 | [**S1_효율적인해킹_BOJ1325**](https://www.acmicpc.net/problem/1325) | [Link](https://github.com/woody35545/Algorithm-study/blob/master/Graph/BOJ_1325_%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8%ED%95%B4%ED%82%B9_RE.py) | Time Out
| 2023.02.03 | [**G5_카드정렬하기_BOJ1715**](https://www.acmicpc.net/problem/1715) | [Link](https://github.com/woody35545/Algorithms/blob/master/Greedy/G5_%EC%B9%B4%EB%93%9C%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0_BOJ1715.py) | Solve
| 2023.02.03 | [**S4_로프_BOJ2217**](https://www.acmicpc.net/problem/2217) | [Link](https://github.com/woody35545/Algorithms/blob/master/Greedy/S4_%EB%A1%9C%ED%94%84_BOJ2217.py) | Solve
## Review
- 2023.01.12 - **BOJ_11725_트리의부모찾기**
  - **`if current_vertex not in visited` 와 `if not visted[current_vertex]` -> 동일한 기능이지만 수행시간에서 차이 발생**  
    `if element in list` 방식의 수행시간이 상대적으로 긴 편
    - [참고]  
       파이썬 자료형 별 시간복잡도: https://wayhome25.github.io/python/2017/06/14/time-complexity/    
  

 
  - **`input()`, `print()` -> `sys.stidn.readline()`, `sys.stdout.write()` 를 사용하면 수행시간 줄어듦**  
      - [참고]   
        https://urakasumi.tistory.com/m/273
        
  - **반복문을 통해 리스트의 특정 인덱스 삭제(pop)시 구현방식에 따라서 일부을 값이 순회에서 누락될 수 있음에 주의** (./Implements/S5_덩치_BOJ7568_.py 참고)
 
  - **파이썬의 `PriorityQueue`와 `heapq`**
    - PriorityQueue는 내부적으로 heapq를 사용한다. heapq는 thread-safe하지 않기 때문에, PriorityQueue는 heapq에다 thread-safe한 동작을 보장하기 위한 일련의 작업들이 더 추가된 것으로 볼 수 있다.
      이 때문에 PriorityQueue를 사용하면 heapq를 사용하는 것보다 수행 시간 측면에서 느리다. 코딩테스트에서는 멀티스레드를 사용할 일이 없기 때문에 항상 heapq를 사용하는 것이 좋다고 생각한다.
