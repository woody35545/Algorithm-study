import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        StringBuilder sb = new StringBuilder();

        // 테스트 케이스 개수
        int T = Integer.parseInt(br.readLine());

        for(int t=0; t<T; t++) {

            // 지원자 성적 순위에 대한 정보 수
            int N = Integer.parseInt(br.readLine());


            /**
             * ranks[i]: i번째 지원자의 서류, 면접 순위
             * ranks[i][0]: i번째 지원자의 서류 순위
             * ranks[i][1]: i번째 지원자의 면접 순위
             */
            int[][] ranks = new int[N][2]; // last: ranks[N-1][0]

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                // 지원자 성적 정보 입력
                ranks[i][0] = a;
                ranks[i][1] = b;
            }

            // 서류 순위 기준으로 sort
            Arrays.sort(ranks, new Comparator<int[]>() {
                @Override
                public int compare(int[] a, int[] b) {
                    return a[0] - b[0];
                }
            });

            // 최초에는 서류순위가 가장 높은 지원자의 면접 순위를 기준으로 비교
            int compareStandard = ranks[0][1];

            // 선발된 지원자 수, 서류가 1등인 지원자는 당연히 선발되기 때문에 1부터 count 시작
            int count = 1;

            // 서류가 높은 순위부터 시작해서 면접 순위 비교
            for (int i = 1; i < ranks.length; i++) {
                if (ranks[i][1] < compareStandard) {
                    // 면접 순위가 현재 기준보다 높다면 선발 카운트 증가
                    count++;

                    // 기준을 현재 지원자의 면접 순위로 변경
                    compareStandard = ranks[i][1];
                }
            }
            sb.append(count).append("\n");
        }
        System.out.print(sb);
    }
}
