import java.io.*;
import java.util.*;

public class Main{


    static StringBuilder resultSb = new StringBuilder(); /* 412355 : StringBuilder  */
    static List<String> results = new ArrayList<>();
    static String[] conditions; // 부등호 조건
    static boolean[] visited = new boolean[10]; // 같은 수 중복 방지를 위한 방문 배열
    static int N; // 부등호 개수
    static boolean isValid(String condition, int a, int b){
        // condition : [ "<" | ">" ]
        if(condition.equals(">"))
            return a > b;
        else if(condition.equals("<"))
            return a < b;

        else
            return false;
    }

    static void backtracking(int depth, int prev){
        if(depth == N+1){
            results.add(resultSb.toString());
            return;
        }

        for(int i=0; i<10; i++){
            if(!visited[i]){ // 동일한 숫자 중복 방지
                if(depth == 0 || isValid(conditions[depth-1], prev, i)){

                    visited[i] = true;
                    resultSb.append(i);
                    backtracking(depth+1, i);

                    resultSb.deleteCharAt(resultSb.length()-1);
                    visited[i] = false;
                }
            }
        }
    }


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        conditions = new String[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0; i<N; i++){
            conditions[i] = st.nextToken();
        }

        backtracking(0, 0);

        StringBuilder sb = new StringBuilder();

        // 최대 최소 출력
        sb.append(results.get(results.size()-1)).append("\n");
        sb.append(results.get(0));

        System.out.print(sb.toString());
    }
}
