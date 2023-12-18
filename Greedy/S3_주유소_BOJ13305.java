import java.io.*;
import java.util.*;

class Node{
    long cost;
    long distanceToNext;

    public Node(int cost, int distanceToNext) {
        this.cost = cost;
        this.distanceToNext = distanceToNext;
    }
}
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());

        // 전체 거리를 이동하는동안 나온 주유비 총합
        long result = 0L;

        Node[] nodes = new Node[N];

        // 노드 배열 초기화
        for(int i=0; i<nodes.length; i++){
            nodes[i] = new Node(0,0);
        }

        // distance와 cost 초기화
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N-1; i++){
            nodes[i].distanceToNext = Long.parseLong(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            nodes[i].cost = Long.parseLong(st.nextToken());
        }


        long cur = nodes[0].cost;
        result += cur * nodes[0].distanceToNext;


        for(int i=1; i<N-1; i++){
            long next = nodes[i].cost;

            if(cur <= next){
                // 현재 위치와 가격이 같거나 다음 지점이 더 비싸면, 현재 위치보다 더 싼 지점이 나올때까지 해당 거리를 현재 가격으로 주유
                result += cur * nodes[i].distanceToNext;
            }
            else if(cur > next){
                // 더 싼 지점이 나왔다면 cur 갱신 및 갱신된 값으로 주유
                cur = next;
                result += cur * nodes[i].distanceToNext;

            }
        }

        System.out.print(result);

    }
}
