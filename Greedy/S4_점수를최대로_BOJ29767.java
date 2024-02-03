import java.io.*;
import java.util.*;
public class Main {
    /*
    그리디로 접근하는 문제이다.
    부분합(prefixSum)을 구한 후에 부분합이 큰 순서대로 정렬하고,
    정렬된 부분합으로부터 가장 큰값부터 K를 뽑아주면 최대가 된다.
     */
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 교실 수
        int N = Integer.parseInt(st.nextToken());
        // 학생 수
        int K = Integer.parseInt(st.nextToken());

        Long[] prefixSum = new Long[N];

        st = new StringTokenizer(br.readLine());

        prefixSum[0] = Long.parseLong(st.nextToken());

        for(int i=1; i<N; i++){
            prefixSum[i] = prefixSum[i-1] + Long.parseLong(st.nextToken());

        }

        // prefixSum 정렬
        Arrays.sort(prefixSum, Collections.reverseOrder());

        long result = 0;
        for(int i=0; i<K; i++){
            result += prefixSum[i];
        }
        System.out.print(result);
    }
}
