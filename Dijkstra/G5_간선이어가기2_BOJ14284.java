import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 정점 개수
        int N = Integer.parseInt(st.nextToken());

        // 간선 수
        int M = Integer.parseInt(st.nextToken());


        ArrayList<Node>[] adjLists = new ArrayList[N+1];

        // 인접 리스트 배열 초기화
        for(int i=0; i<adjLists.length; i++){
            adjLists[i] = new ArrayList<>();
        }

        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            // 무방향 그래프
            adjLists[u].add(new Node(v,w));
            adjLists[v].add(new Node(u,w));

        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int target = Integer.parseInt(st.nextToken());

        // distance 배열 초기화
        int[] dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        // 방문 배열 초기화
        boolean[] visited = new boolean[N+1];

        PriorityQueue<Node> pq = new PriorityQueue<>(new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return o1.weight - o2.weight;
            }
        });

        pq.add(new Node(start, 0));
        dist[start] = 0;
        visited[start] = true;

        while(!pq.isEmpty()){
            Node currentNode = pq.remove();
            int currentNodeNumber = currentNode.number;

            // 다음 노드 탐색
            for(int i=0; i<adjLists[currentNodeNumber].size(); i++){
                Node nextNode = adjLists[currentNodeNumber].get(i);
                int nextNodeNumber = nextNode.number;
                int weightToNext = nextNode.weight;

                if(!visited[nextNodeNumber]
                        && dist[nextNodeNumber] > dist[currentNodeNumber] + weightToNext){
                    dist[nextNodeNumber] = dist[currentNodeNumber] + weightToNext;
                    pq.add(new Node(nextNodeNumber, dist[nextNodeNumber]));
                }
            }
        }

        System.out.print(dist[target]);
    }
}

class Node{
    int number;
    // 이전 노드에서 현재 노드까지 간선 비용
    int weight;

    public Node(int number, int weight) {
        this.number = number;
        this.weight = weight;
    }
}
