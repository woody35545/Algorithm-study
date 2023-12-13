import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    static HashSet<Integer> integerSet = new HashSet<>();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());

        for(int i=0; i<N; i++){
            integerSet.add(Integer.parseInt(st.nextToken()));
        }

        ArrayList<Integer> integerList = new ArrayList<>(integerSet);

        Collections.sort(integerList);

        for(var elem : integerList){
            sb.append(elem).append(" ");
        }
        System.out.print(sb);
    }
}
