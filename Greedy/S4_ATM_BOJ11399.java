import java.io.*;
import java.util.*;

/*
 * 돈을 인출할때 걸리는 시간이 적을 수록 앞에 배치하는 것이 무조건 유리하다.
 * 따라서 돈을 인출할때 걸리는 시간별로 사람을 정렬한 상태에서, 
 * 순차적으로 각 사람의 인출시간을 구해 결과를 도출하면 된다.
 */
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        int N = Integer.parseInt(br.readLine());
        int[] times = new int[N];
        int[] timeAccSum = new int[N];

        st = new StringTokenizer(br.readLine());


        for(int i=0; i<times.length; i++){
            times[i] = Integer.parseInt(st.nextToken());
        }

        // 걸리는 시간순으로 정렬
        Arrays.sort(times);

        // 누적 합 배열 초기화
        int tempSum = 0;
        for(int i=0; i<times.length; i++){
            tempSum += times[i];
            timeAccSum[i] = tempSum;
        }

        int totalSum = 0;

        // 각 누적합 전부 더해줌
        for(int i=0; i<times.length; i++){
            totalSum += timeAccSum[i];
        }

        System.out.print(totalSum);

    }
}
