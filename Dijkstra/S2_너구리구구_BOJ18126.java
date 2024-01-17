import java.io.*;
import java.util.*;

/*
다익스트라로 풀어주었다. 
양방향 그래프이기 때문에 다음 노드들 확인할 때 이미 방문한 지점이면 갱신 하지 않도록 조건을 주어야 맞다고 처리된다. 
그런데 이미 방문했던 노드를 역방향으로 방문하면 당연히 잘못된 값이 나오니까 단방향으로 하면 안되나? 하는 생각에 단방향 그래프로 선언 후 풀었다가 틀렸다. 
단방향으로 구현했을 때 어떤 반례가 발생하는지는 아직 찾지 못했다.
양방향 그래프로 설정한 후 기존에 방문한 지점을 다시 탐색하지 않도록 설정하여 해결하였다.
이 문제는 원래 의도는 BFS를 이용하여 풀라고 의도한 문제인 것 같다.
*/
class Node{
    private static int lastId = 0;
    private static HashMap<Integer, Node> dataNodeMap = new HashMap<>();
    private static HashMap<Integer, Node> idNodeMap = new HashMap<>();

    int id;
    int data;

    private Node(int data){
        this.id = lastId++;
        this.data = data;
    }

    public static Node getNodeByData(int data){
        if(dataNodeMap.containsKey(data)){
            return dataNodeMap.get(data);
        }
        else{
            Node newNode = new Node(data);
            dataNodeMap.put(data, newNode);
            idNodeMap.put(newNode.id, newNode);
            return newNode;
        }
    }
}

class Edge{
    Node startNode;
    Node endNode;
    long weight;

    public Edge(Node startNode, Node endNode, long weight){
        this.startNode = startNode;
        this.endNode = endNode;
        this.weight = weight;
    }
}

public class Main{

    static int N;
    static boolean[] visited;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 노드 개수
        N = Integer.parseInt(br.readLine());

        ArrayList<Edge>[] nodeEdgeListArr = new ArrayList[N];

        for(int i=0; i<N; i++){
            nodeEdgeListArr[i] = new ArrayList<>();
        }

        for(int i=0; i<N-1; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long weight = Long.parseLong(st.nextToken());

            Node nodeA = Node.getNodeByData(a);
            Node nodeB = Node.getNodeByData(b);

            // 양방향
            Edge edge1 = new Edge(nodeA, nodeB, weight);
            Edge edge2 = new Edge(nodeB, nodeA, weight);

            nodeEdgeListArr[nodeA.id].add(edge1);
            nodeEdgeListArr[nodeB.id].add(edge2);
        }

        // 거리 배열 초기화
        long[] distance = new long[N];
        Arrays.fill(distance, Integer.MIN_VALUE);
        distance[Node.getNodeByData(1).id] = 0;

        // 방문 배열 초기화
        boolean[] visited = new boolean[N];

        // 가중치 큰 값을 먼저 뽑기 위해 우선순위 큐 사용
        PriorityQueue<Edge> pq = new PriorityQueue<>((edge1, edge2) -> -Long.compare(edge1.weight, edge2.weight));

        // 시작 노드 초기화
        pq.add(new Edge(null, Node.getNodeByData(1), 0));

        while(!pq.isEmpty()){
            Edge popped = pq.poll();
            Node currentNode = popped.endNode;

            if(visited[currentNode.id]) {
                System.out.println(String.format("%d는 이미 방문한 노드 입니다.", currentNode.data));
                continue;
            }

            visited[currentNode.id] = true;

            for(int i=0; i<nodeEdgeListArr[currentNode.id].size(); i++){
                Edge edge = nodeEdgeListArr[currentNode.id].get(i);
                Node nextNode = edge.endNode;
                if(distance[nextNode.id] < distance[currentNode.id] + edge.weight && !visited[nextNode.id]){
                    // 값이 더 크면 갱신
                    distance[nextNode.id] = distance[currentNode.id] + edge.weight;

                    pq.add(new Edge(currentNode, nextNode, distance[nextNode.id]));
                }
            }
        }

        Arrays.sort(distance);
        System.out.print(distance[N-1]);
    }
}
