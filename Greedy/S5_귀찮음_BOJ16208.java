import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    /**
     * 필요한 막대중 작은 것부터 만든다. 그래야 비용이 최소가 된다.
     */
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


    public static void main(String[] args) throws IOException {


        // 필요한 막대 개수
        int N = Integer.parseInt(br.readLine());
        int[] stickLength = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        int totalLength = 0;
        for(int i=0; i<N; i++){
            stickLength[i] = Integer.parseInt(st.nextToken());
            totalLength += stickLength[i];
        }

        // 필요한 막대 길이가 짧은 순으로 정렬
        Arrays.sort(stickLength);
        int cur = 0;
        long cost = 0L;
        while(totalLength > 0) {
            int need = stickLength[cur];
//            System.out.println(String.format("필요한 막대길이: %d", stickLength[cur]));

            // 긴막대에서 필요한 막대만큼 분할
            totalLength -= need;

            cost += (long) need * totalLength;
            cur++;
        }
        System.out.print(cost);
    }

}
