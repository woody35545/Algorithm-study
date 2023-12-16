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

    // 중복해서 뽑지 않기 위한 방문 리스트
    static ArrayList<Integer> visitedList = new ArrayList<>();
		// 중복되는 결과값이 존재하지 않도록 하기 위해 LinkedHashSet에 저장
    static Set<String> resultHashSet = new LinkedHashSet<>();

    static void backtracking(int depth){
        if(depth == M){
            sb = new StringBuilder();
            for(var elem : results){
                sb.append(elem).append(" ");
            }

            resultHashSet.add(sb.toString());

            return;
        }

        for(int i=0; i<numbers.size(); i++){
            int current = numbers.get(i);
            if(!visitedList.contains(i)){
                visitedList.add(i);
                results.add(current);
                backtracking(depth+1);
                visitedList.remove(Integer.valueOf(i));
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

        backtracking(0);

        sb = new StringBuilder();
        for(var elem : resultHashSet){
            sb.append(elem).append("\n");
        }

        System.out.print(sb);

    }
}
