import java.io.*;
import java.util.*;

public class Main{
    static int[] result;
    static boolean[] visited;
    static int N;
    static int M;
    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 수열을 담을 배열
        result = new int[M];

        // 1부터 N까지의 각 수들의 방문 여부(중복해서 뽑지 않기 위함)
        visited = new boolean[N+1];


        // depth는 0부터 시작, N은 1부터 시작이므로 초기 prev 값은 그보다 작은 0으로 초기화
        dfs(0,0);
        System.out.print(sb);
    }

    static void dfs(int depth, int prev){
        if(depth == M){
            for(int i=0; i<result.length; i++){
                sb.append(result[i]).append(" ");
            }
            sb.append("\n");
        return;
        }

        for(int i=1; i<N+1; i++){
            // 중복을 방지하기 위해 방문하지 않았는지 확인하고
            // 현재 방문하려는 수가 이전에 방문한 수보다 큰지 확인(오름차순 수열 조건을 만족하기 위함)
            if(!visited[i] && i > prev){
                // 방문하지 않았다면 방문처리 후 수열(result)에 추가
                visited[i] = true;
                result[depth] = i;

                // 다음 depth도 탐색, 다음 depth의 prev는 현재 i
                dfs(depth+1, i);

                // 다른 수도 확인해보기 위해 다음 depth에 대해 재귀호출 후 방문처리 해제
                visited[i] = false;
            }
        }
    }
}
