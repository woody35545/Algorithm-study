import java.io.*;
import java.util.*;

public class Main{
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder resultSb = new StringBuilder();
    static String A;
    static int B;

    static List<Integer> visited = new ArrayList<>(); /* visited.add(2) ~> visited A.charAt(2) */
    static List<String> resultList = new ArrayList<>();

    static void backtracking(int depth){
        if(depth == A.length() &&
                Integer.parseInt(resultSb.toString()) < B &&
                resultSb.charAt(0) != '0' // C는 0으로 시작하면 안됨
        )
        {
            resultList.add(resultSb.toString());
            return;
        }

        for(int i=0; i<A.length(); i++){
            int cur = Character.getNumericValue(A.charAt(i));

            if(!visited.contains(i)){
                visited.add(i);
                resultSb.append(cur);
                backtracking(depth+1);

                resultSb.deleteCharAt(resultSb.length()-1);
                visited.remove(Integer.valueOf(i));
            }
        }
    }

    public static void main(String[] args) throws IOException{

        st = new StringTokenizer(br.readLine());

        A = st.nextToken(); /* 1234 : String */
        B = Integer.parseInt(st.nextToken()); /* 3456 : int */

        backtracking(0);

        Collections.sort(resultList);

        if(resultList.size() == 0){
            System.out.print("-1");
        }
        else{
            System.out.print(resultList.get(resultList.size()-1));
        }
    }
}
