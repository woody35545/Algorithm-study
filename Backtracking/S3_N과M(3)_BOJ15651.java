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

        // 1부터 N까지 자연수 중에서 중복을 허용하여 M개를 선택한 수열
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 수열을 담을 배열
        result = new int[M];

        // depth는 0부터 시작
        dfs(0);
        System.out.print(sb);
    }

    static void dfs(int depth){
        if(depth == M){
            for(int i=0; i<result.length; i++){
                sb.append(result[i]).append(" ");
            }
            sb.append("\n");
        return;
        }

        for(int i=1; i<N+1; i++){
                // 같은수가 중복되어 선택할 수 있으므로 visited를 확인하거나 고려하지 않아도 됨
                result[depth] = i;

                dfs(depth+1);
        }
    }
}
