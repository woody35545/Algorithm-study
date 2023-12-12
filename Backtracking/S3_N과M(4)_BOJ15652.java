import java.io.*;
import java.util.*;

public class Main{
    static int[] result;
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

        // depth는 0부터 시작, N은 1부터 시작이므로 초기 prev 값은 그보다 작은 0으로 초기화
        dfs(0, 0);
        System.out.print(sb);
    }


    // prev는 비내림차순을 만족하기 위한 변수
    static void dfs(int depth, int prev){
        if(depth == M){
            for(int i=0; i<result.length; i++){
                sb.append(result[i]).append(" ");
            }
            sb.append("\n");
        return;
        }

        for(int i=1; i<N+1; i++){
            // 중복을 허용하므로 visited는 고려할 필요가 없음
            // 비내림차순을 만족하는 경우만 탐색하기 위해, prev보다 크거나 같은 경우만 탐색
            if(i >= prev) {
                result[depth] = i;
                dfs(depth + 1, i);
            }
        }
    }
}
