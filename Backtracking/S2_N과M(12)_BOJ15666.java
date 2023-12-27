import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();
    static ArrayList<Integer> numberList = new ArrayList<>();
    static ArrayList<Integer> visitedList = new ArrayList<>();
  
    // 각 단계별 결과를 임시로 저장하기 위한 리스트
    static ArrayList<Integer> stepResultList = new ArrayList<>();

    static LinkedHashSet<String> globalResultSet = new LinkedHashSet<>();

    static int N;
    static int M;


    public static void backtracking(int depth, int prev){

        if(depth == M){
            sb = new StringBuilder();
            for(var elem : stepResultList){
                sb.append(elem).append(" ");
            }// sb ~> 1 3
            globalResultSet.add(sb.toString());
            return;
        }

        for(int i=0; i<numberList.size(); i++){
            int current = numberList.get(i);

            if(prev <= current){
                stepResultList.add(current);
                backtracking(depth+1, current);
                stepResultList.remove(stepResultList.size()-1);
            }
        }


    }
    public static void main(String[] args) throws IOException{
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        while(st.hasMoreTokens()){
            numberList.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(numberList);
        backtracking(0,0);

        sb = new StringBuilder();
        for(var e : globalResultSet){
            sb.append(e).append("\n");
        }

        System.out.print(sb);

    }

}
