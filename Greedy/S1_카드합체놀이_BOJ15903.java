import java.io.*;
import java.util.*;

public class Main {
    /*
    점수가 최소가 되려면 매번 가장 작은 카드를 합쳐야 함.
    카드를 합치면 합친 값으로 두 카드의 값을 갱신하므로,
    카드의 값들이 자주 변하는 상황에서 빠르게 최솟값을 찾기 위해서 우선순위 큐를 사용
     */

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        // 작은 값을 우선으로 반환하는 우선순위큐
        PriorityQueue<Long> pq = new PriorityQueue<>();

        st = new StringTokenizer(br.readLine());

        // 카드의 개수
        int N = Integer.parseInt(st.nextToken());

        // 합치는 횟수
        int M = Integer.parseInt(st.nextToken());

        // 우선순위큐 초기화
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            pq.add(Long.parseLong(st.nextToken()));
        }

        // 카드 합치기 M회
        for(int i=0; i<M; i++){
            // 가장 작은 카드 두개 꺼냄
            long min1 = pq.remove();
            long min2 = pq.remove();
            long sum = min1 + min2;

            // 두 카드를 더한 값으로 각각 갱신하여 다시 큐에 넣어줌
            pq.add(sum);
            pq.add(sum);
        }

        // 큐에 있는 카드의 총 합
        long result = 0;

        // 큐의 크기는 remove 하면서 계속 변하므로 밖에다 선언
        int pqSize = pq.size();
        for(int i=0; i<pqSize; i++){
            result += pq.remove();
        }
        System.out.print(result);
    }
}
