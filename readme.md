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


## Today I Tried or Solved
|Date|Title|Code|Description|
|:---:|:---:|:---:|:---:|
| 2023.01.30 | [**G4_최단경로찾기_BOJ1753**](https://www.acmicpc.net/problem/4963)| [Link](https://github.com/woody35545/Algorithm/blob/master/Dijkstra/G4_%EC%B5%9C%EB%8B%A8%EA%B2%BD%EB%A1%9C_BOJ1753.py) |Python3는 통과하는데 Pypy로는 왜 시간초과가 날까..? 
| 2023.01.31 | [**S1_효율적인해킹_BOJ1325**](https://www.acmicpc.net/problem/1325) | - | Time Out
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
