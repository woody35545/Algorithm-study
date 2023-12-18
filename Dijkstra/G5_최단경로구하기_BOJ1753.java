import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {


    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 노드 개수
        int V = Integer.parseInt(st.nextToken());

        // 간선 개수
        int E = Integer.parseInt(st.nextToken());

        // 시작 노드 번호
        int startNodeNumber = Integer.parseInt(br.readLine());

        // 인접 노드 리스트
        ArrayList<Node>[] adjNodeList = new ArrayList[V+1];

        // 다익스트라를 위한 거리 배열
        int[] distance = new int[V+1];

        // 가장 큰값으로 초기화
        Arrays.fill(distance, Integer.MAX_VALUE);

        for(int i=1; i<=V; i++){
            adjNodeList[i] = new ArrayList<>();
        }


        for(int i=0; i<E; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            adjNodeList[u].add(new Node(v, w));
        }


        // 다익스트라
        PriorityQueue<Node> queue = new PriorityQueue<>(new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return o1.weight - o2.weight;
            }
        });
        boolean[] visited = new boolean[V+1];
        queue.add(new Node(startNodeNumber, 0));
        distance[startNodeNumber] = 0;

        while(!queue.isEmpty()){
            Node currentNode = queue.remove();
            
            if(visited[currentNode.number]) continue;
            visited[currentNode.number] = true;
            
            for(Node nextNode : adjNodeList[currentNode.number]){
                if(distance[nextNode.number] > distance[currentNode.number] + nextNode.weight){
                    distance[nextNode.number] = distance[currentNode.number] + nextNode.weight;
                    queue.add(new Node(nextNode.number, distance[nextNode.number]));
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int i=1; i<distance.length; i++){
            if(distance[i] == Integer.MAX_VALUE){
                sb.append("INF").append("\n");
            }
            else{
                sb.append(distance[i]).append("\n");
            }
        }
        System.out.print(sb);
    }
}

class Node{
    int number;
    int weight;

    public Node(int number, int weight) {
        this.number = number;
        this.weight = weight;
    }
}
