// 문제 출처: https://www.codetree.ai/missions/2/problems/tromino?&utm_source=clipboard&utm_medium=text

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

        // init array
        int[][] map = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // init max sum
        int maxSum = -1;

        // 'ㄱ' 자 형 모양에서 나올 수 있는 최대합 계산
        for (int i = 0; i <= N - 2; i++) {
            for (int j = 0; j <= M - 2; j++) {
                int tempSum1 = map[i][j] + map[i + 1][j] + map[i + 1][j + 1];
                int tempSum2 = map[i][j] + map[i][j + 1] + map[i + 1][j + 1];
                int tempSum3 = map[i][j + 1] + map[i + 1][j + 1] + map[i + 1][j];
                int tempSum4 = map[i][j] + map[i][j + 1] + map[i + 1][j];

                // 최대값으로 maxSum 갱신
                maxSum = Math.max(maxSum, Math.max(Math.max(tempSum1, tempSum2), Math.max(tempSum3, tempSum4)));
            }
        }

        // 'ㅣ' 자형 모양에서 나올 수 있는 최대합 계산
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= M - 3; j++) {
                int tempSum = 0;
                for (int k = j; k < j + 3; k++) {
                    tempSum += map[i][k];
                }
                maxSum = Math.max(maxSum, tempSum);
            }
        }

        for (int j = 0; j < M; j++) {
            for (int i = 0; i <= N - 3; i++) {
                int tempSum = 0;
                for (int k = i; k < i + 3; k++) {
                    tempSum += map[k][j];
                }
                maxSum = Math.max(maxSum, tempSum);
            }
        }
        
        System.out.print(maxSum);
    }
}
