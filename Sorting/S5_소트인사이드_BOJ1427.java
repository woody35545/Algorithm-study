import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws IOException {
        /* {"2", "1", "4", "3"} */
        String[] tokens = br.readLine().split("");

        Integer[] integerArr = new Integer[tokens.length];
        for(int i=0; i<tokens.length; i++){
            integerArr[i] = Integer.parseInt(tokens[i]);
        }

        Arrays.sort(integerArr, Collections.reverseOrder());

        for(var elem : integerArr){
            sb.append(elem);
        }

        System.out.print(sb);
    }
}
