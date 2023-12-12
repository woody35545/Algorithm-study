import java.io.*;
import java.util.*;

public class Main{
    static int[] result;
    static int N;
    static int M;
    static List<Integer> visited = new ArrayList<>();
    static int[] choices;
    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());


        // 선택할 수 있는 숫자를 담을 배열
        choices = new int[N];
        st = new StringTokenizer(br.readLine());
        int cur = 0;
        while(st.hasMoreTokens()){
            choices[cur] = Integer.parseInt(st.nextToken());
            cur ++;
        }

        Arrays.sort(choices); // 오름차순으로 방문하기 위해 정렬

        // 수열을 담을 배열
        result = new int[M];

        dfs(0, -1);
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

        for(int i=0; i<choices.length; i++){
            int cur = choices[i];

            if(!visited.contains(cur) && prev <= cur) {
                // 오름차순 유지를 위한 조건
                visited.add(cur);
                result[depth] = cur;
                dfs(depth + 1, cur);

                visited.remove(Integer.valueOf(cur));
            }
        }
    }
}
