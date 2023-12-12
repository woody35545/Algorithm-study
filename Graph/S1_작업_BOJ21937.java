import java.io.*;
import java.util.*;

public class Main{
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

    static int N;
    static int M;

    static int dfs(int start){
        Stack<Integer> stack = new Stack<>();
        boolean[] visited = new boolean[N+1];
        stack.push(start);
        visited[start] = true;
        int count = 0;
        while(!stack.empty()){

            int cur = stack.pop();

            for(int i=0; i<graph.get(cur).size(); i++){
                int neighbor = graph.get(cur).get(i);
                if(!visited[neighbor]){
                    count ++;
                    visited[neighbor] = true;
                    stack.push(neighbor);
                }
            }
        }

        return count;
    }
    public static void main(String[] args) throws IOException{
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for(int i=0; i<N+1; i++){
            graph.add(new ArrayList<>());
        }


        // 그래프 정보 초기화
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(b).add(a);
        }


        int target = Integer.parseInt(br.readLine());

        System.out.print(dfs(target));

    }
}
