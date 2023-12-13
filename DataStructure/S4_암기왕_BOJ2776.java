import java.io.*;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());

            HashMap<Integer, Integer> map = new HashMap<>();

            st = new StringTokenizer(br.readLine());

            for (int i = 0; i < N; i++) {
                map.put(Integer.parseInt(st.nextToken()), 0);
            }

            int M = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine());


            for (int i = 0; i < M; i++) {
                int current = Integer.parseInt(st.nextToken());

                if (map.containsKey(current)) {
                    sb.append(1).append("\n");
                } else {
                    sb.append(0).append("\n");
                }
            }
        }
        System.out.print(sb);
    }
}
