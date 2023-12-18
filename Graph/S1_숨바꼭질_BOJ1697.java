import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();
    static final int MAX_SIZE = 100_001;
    static int N;
    static int K;

    public static int[] bfs(int start){
        Queue<Integer> queue = new LinkedList<>();
        int[] visited = new int[MAX_SIZE];
        Arrays.fill(visited, -1);

        queue.add(start);
        visited[start] = 0;

        while(queue.size() > 0){
            int current = queue.remove();
            int next;

            if(0<=current-1 && current-1<MAX_SIZE && visited[current-1] == -1){
                next = current - 1;
                visited[next] = visited[current] + 1;
                if(next == K) return visited;
                queue.add(next);
            }

            if(0<=current+1 && current+1<MAX_SIZE && visited[current+1] == -1){
                next = current + 1;
                visited[next] = visited[current] + 1;
                if(next == K) return visited;
                queue.add(next);
            }

            if(0<=2*current && 2*current<MAX_SIZE && visited[2*current] == -1){
                next = 2*current;
                visited[next] = visited[current] + 1;
                if(next == K) return visited;

                queue.add(next);
            }
        }
        return visited;
    }

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        System.out.print(bfs(N)[K]);

    }
}
