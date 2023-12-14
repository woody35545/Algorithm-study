import java.io.*;
import java.util.*;

class Pos{
    int x;
    int y;

    public Pos(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    // 그래프에서 탐색 가능한 방향
    static int[] dx = new int[] {-1,1,0,0};
    static int[] dy = new int[] {0,0,-1,1};

    // 그래프 크기(N x M)
    static int N;
    static int M;

    // 이동할 수 있는 최대 높이 차이
    static int K;

    // 방문 처리를 위한 배열
    static boolean[][] visited;

    static int[][] graph;

    public static void dfs(int startX, int startY){
        Stack<Pos> stack = new Stack<>();

        // 시작점을 stack에 넣고 방문처리
        stack.push(new Pos(startX, startY));
        visited[startX][startY] = true;

        while(!stack.isEmpty()){
            Pos currentPos = stack.pop();

            for(int i=0; i<dx.length; i++){
                int nextX = currentPos.x + dx[i];
                int nextY = currentPos.y + dy[i];

                if(0 <= nextX && nextX<N && 0<= nextY && nextY<M
                        && !visited[nextX][nextY]
                        && Math.abs(graph[currentPos.x][currentPos.y] - graph[nextX][nextY]) <= K){

                    stack.push(new Pos(nextX, nextY));
                    visited[nextX][nextY] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());;

        // 그래프 크기 초기화
        graph = new int[N][M];
        // 방문 배열 크기 초기화
        visited = new boolean[N][M];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++){
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int count = 0;
        // 방문하지 않은 지점이 없을 때까지 dfs로 탐색
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(!visited[i][j]){
                    dfs(i, j);
                    count ++;
                }
            }
        }
        System.out.print(count);
    }
}
