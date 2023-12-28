import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    static int[] partialSum;
    static int[] numbers;

    public static void main(String[] args) throws IOException{
        st = new StringTokenizer(br.readLine()); // 5 3
        // 숫자 개수
        int N = Integer.parseInt(st.nextToken());
        // 합을 구해야하는 횟수
        int M = Integer.parseInt(st.nextToken());

        numbers = new int[N];
        partialSum = new int[N];

        st = new StringTokenizer(br.readLine());
        int currentSum = 0;
        for(int i=0; i<N; i++){
            currentSum += Integer.parseInt(st.nextToken());
            partialSum[i] = currentSum;
        }

        // 질의 구간
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine()); // 1 3
            int start = Integer.parseInt(st.nextToken()) - 1;
            int end = Integer.parseInt(st.nextToken()) - 1;

            int result;
            if(start == 0){
                result = partialSum[end];
            }else {
                result = partialSum[end] - partialSum[start - 1];
            }

            sb.append(result).append("\n");
        }

        System.out.print(sb);
    }


}
