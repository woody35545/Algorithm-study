import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    static ArrayList<Integer> results = new ArrayList<>();

    static int N;
    static int M;

    static ArrayList<Integer> numbers = new ArrayList<>();


    static void backtracking(int depth, int prev){
        if(depth == M){
            for(var elem : results){
                sb.append(elem).append(" ");
            }
            sb.append("\n");
            return;
        }

        for(int i=0; i<numbers.size(); i++){
            int current = numbers.get(i);
            if(current >= prev){ // 비 내림차순을 유지하기 위한 조건
                results.add(current);
                backtracking(depth+1, current);
                results.remove(results.size()-1);
            }
        }
    }

    
    public static void main(String[] args) throws IOException{
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        while(st.hasMoreTokens()){
            numbers.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(numbers);

        backtracking(0,0);

        System.out.print(sb);
    }
}
