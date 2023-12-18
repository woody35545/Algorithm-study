import java.io.*;
import java.util.*;

class Point{
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

}
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();
    static int[][] graph;
    static boolean[][] visited;

    static int M;
    static int N;
    static int K;

    static final int[] dx = new int[]{-1,1,0,0};
    static final int[] dy = new int[]{0,0,-1,1};

    public static int dfs(Point startPoint){
        Stack<Point> stack = new Stack<>();
        stack.add(startPoint);
        visited[startPoint.y][startPoint.x] = true;

        int areaSize = 1; // 영역 크기

        while(!stack.isEmpty()){
            Point currentPoint = stack.pop();

            for(int i=0; i< dx.length; i++) {
                int nextX = currentPoint.x + dx[i];
                int nextY = currentPoint.y + dy[i];

                if(0<=nextX && nextX<N && 0<=nextY && nextY<M && graph[nextY][nextX] == 0 && !visited[nextY][nextX]){
                    stack.push(new Point(nextX,nextY));
                    visited[nextY][nextX] = true;
                    areaSize++;
                }
            }
        }
        return areaSize;
    }
    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        graph = new int[M][N];
        visited = new boolean[M][N];

        K = Integer.parseInt(st.nextToken());


        for(int k=0; k<K; k++){
            st = new StringTokenizer(br.readLine());
            int lx = Integer.parseInt(st.nextToken());
            int ly = Integer.parseInt(st.nextToken());
            int rx = Integer.parseInt(st.nextToken());
            int ry = Integer.parseInt(st.nextToken());

            for(int i=ly; i<ry; i++){
                for(int j=lx; j<rx; j++){
                    // 직사각형이 차지하는 영역을 1로 초기화
                    graph[i][j] = 1;
                }
            }
        }

        // 그래프의 모든 좌표들을 돌면서 탐색되지 않은 지점에 대해 dfs 수행
        // 결과로 반환된 각 영역 크기를 resultList에 저장
        int numberOfArea = 0;
        ArrayList<Integer> resultList = new ArrayList<>();
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                if(!visited[i][j] && graph[i][j] == 0){
                    resultList.add(dfs(new Point(j,i)));
                    numberOfArea++;
                }
            }
        }

        Collections.sort(resultList);

        sb.append(numberOfArea).append("\n");
        for(var item : resultList){
            sb.append(item).append(" ");
        }
        System.out.print(sb);

    }
}
