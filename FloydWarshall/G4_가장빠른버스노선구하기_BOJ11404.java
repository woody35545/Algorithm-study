import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        // distance[i][j] -> i에서 j로 가는 최소거리
        int[][] distance = new int[N+1][N+1];
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                if(i==j){
                    distance[i][j] = 0;
                }
                else{
                // 충분히 큰 수로 초기화
                    distance[i][j] = 10000001;
                }

            }
        }

        // distance 초기화
        for(int i=0; i<M; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            if(distance[u][v] > w) distance[u][v] = w;
        }

        // k -> 경유지
        for(int k=1; k<=N; k++){
            for(int i=1; i<=N; i++){
                for(int j=1; j<=N; j++){
                    if(distance[i][j] > distance[i][k] + distance[k][j]){
                        distance[i][j] = distance[i][k] + distance[k][j];
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        // 도시 i에서 j로 가넨드 필요한 최소비용 출력, 갈수없다면 0 출력
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                if(distance[i][j] == 10000001){
                    sb.append(0).append(" ");
                }
                else{
                    sb.append(distance[i][j]).append(" ");
                }
            }
            sb.append("\n");
        }

        System.out.print(sb);

    }
}
