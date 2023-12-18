import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    static String[] names;
    public static void main(String[] args) throws IOException {

        int N = Integer.parseInt(br.readLine());
        names = new String[N];
        for(int i=0; i<N; i++){
            names[i] = br.readLine();
        }

        String[] tmp = Arrays.copyOfRange(names, 0,names.length);

        // 오름차순인지 확인
        Arrays.sort(tmp);
        if(Arrays.equals(names, tmp)){
            sb.append("INCREASING");
        }
        else{
            // 내림차순인지 확인
            Arrays.sort(tmp, Collections.reverseOrder());
            if(Arrays.equals(names, tmp)){
                sb.append("DECREASING");
            }
            else{
                sb.append("NEITHER");
            }
        }

        System.out.print(sb);
    }
}
