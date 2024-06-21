/*
 * 문제 출처: https://www.codetree.ai/missions/2/problems/number-of-happy-sequence?&utm_source=clipboard&utm_medium=text
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // init N, M
        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // N x N array
        int[][] map = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 행복한 수열 개수 초기화
        int totalCount = 0;

        if (M == 1) {
            /* 
              M이 1인 경우 행복한 수열 개수 = (행 개수 + 열 개수)가 되므로,
              반복문을 통해 확인할 필요없이 N x N 에서 행 개수(N개) + 열 개수(N개)인 2 * N 으로 초기화 
            */
            totalCount = 2 * N;
        } else {

            // 각 행에서 행복한 수열 카운트
            for (int i = 0; i < N; i++) {
                // 현재 행에서 연속된 수의 개수
                int tempCount = 1;

                for (int j = 1; j < N; j++) {
                    if (map[i][j - 1] == map[i][j]) {
                        tempCount++;
                    } else {
                        tempCount = 1;
                    }

                    if (tempCount >= M) {
                        totalCount++;
                        break;
                    }
                }
            }

            // 각 열에서 행복한 수열 카운트
            for (int j = 0; j < N; j++) {
                // 현재 열에서 연속된 수의 개수
                int tempCount = 1;

                for (int i = 1; i < N; i++) {
                    if (map[i - 1][j] == map[i][j]) {
                        tempCount++;
                    } else {
                        tempCount = 1;
                    }

                    if (tempCount >= M) {
                        totalCount++;
                        break;
                    }
                }
            }
        }

        System.out.print(totalCount);
    }
}
