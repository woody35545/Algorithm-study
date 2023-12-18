import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] graph;
    static int N;
    static int M;

    // index 0: up, 1: down, 2: left, 3: right
    static int[] dx = new int[]{-1,1,0,0};
    static int[] dy = new int[]{0,0,-1,1};

    // 방문 확인을 위한 배열
    static boolean[][] visited;
    // 사이클 판단을 위한 배열
    static boolean[][] finished;
    static int safeZoneCount = 0;
    static void dfs(int sx, int sy){

        visited[sx][sy] = true;

        int currentDirection = graph[sx][sy];

        // 다음 좌표
        int nx = sx + dx[currentDirection];
        int ny = sy + dy[currentDirection];

        // 유효한 좌표일 경우만 진행
        if(!(0 <= nx && nx < N && 0 <= ny && ny < M))
            return;

        if(!visited[nx][ny] ){
            dfs(nx,ny);
        }else{
            // 이전에 방문했던 지점으로 다시 돌아왔다면, safezone 카운트를 센적 있는지 확인
            // 센적이 없다면 safezone 카운트 증가
            if(!finished[nx][ny]) safeZoneCount++;
        }

        finished[sx][sy] = true;
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new int[N][M];
        visited = new boolean[N][M];
        finished = new boolean[N][M];

        // 그래프 문자에 따라서 방향 인덱스 값으로 초기화
        for(int i=0; i<N; i++){
            String inputLine = br.readLine();
            for(int j=0; j<M; j++){
                char curChar = inputLine.charAt(j);

                if(curChar == 'U'){
                    graph[i][j] = 0;
                }else if(curChar == 'D'){
                    graph[i][j] = 1;
                }else if(curChar == 'L'){
                    graph[i][j] = 2;
                }else if(curChar == 'R'){
                    graph[i][j] = 3;
                }
            }
        }

        // 방문하지 않은 모든 점에 대해서 dfs
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(!visited[i][j]){
                    dfs(i,j);
                }
            }
        }

        System.out.print(safeZoneCount);
    }
}
