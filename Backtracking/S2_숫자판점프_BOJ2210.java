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

    static final int[] dx = new int[]{-1,1,0,0};
    static final int[] dy = new int[]{0,0,-1,1};
    static HashSet<String> resultSet = new HashSet();

    public static void dfs(Point startPoint, int travelCount, StringBuilder sb){

            if(travelCount <= 6) {

                for (int i = 0; i < dx.length; i++) {
                    int nextX = startPoint.x + dx[i];
                    int nextY = startPoint.y + dy[i];

                    if (0 <= nextX && nextX < 5 && 0 <= nextY && nextY < 5) {
                        sb.append(graph[nextY][nextX]);
                        dfs(new Point(nextX,nextY), travelCount+1, sb);
                        sb.deleteCharAt(sb.length()-1);
                    }
                }
            }
            else{
                resultSet.add(sb.toString());
                return;
            }

    }
    public static void main(String[] args) throws IOException {
        graph = new int[5][5];
        for(int i=0; i<5; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<5; j++){
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for(int i=0; i<5; i++){
            for(int j=0; j<5; j++){
                dfs(new Point(j,i), 1, new StringBuilder());
            }
        }


        System.out.print(resultSet.size());
    }
}
