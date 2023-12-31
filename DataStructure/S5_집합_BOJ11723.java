import java.io.*;
import java.util.*;
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        HashSet<String> set = new HashSet();
        StringBuilder sb = new StringBuilder();
        int M = Integer.parseInt(br.readLine());

        for (int i = 0; i < M; i++) {
            String[] tokens = br.readLine().split(" ");

            if (tokens[0].equals("add")) {
                set.add(tokens[1]);
            } else if (tokens[0].equals("check")) {
                if (set.contains(tokens[1])) {
                    sb.append("1").append("\n");
                } else {
                    sb.append("0").append("\n");
                }
            } else if (tokens[0].equals("remove")) {
                set.remove(tokens[1]);
            } else if (tokens[0].equals("toggle")) {
                if(set.contains(tokens[1])){
                    set.remove(tokens[1]);
                }else{
                    set.add(tokens[1]);
                }
            } else if (tokens[0].equals("empty")) {
                set = new HashSet<>();
            } else if (tokens[0].equals("all")) {
                set = new HashSet<>();
                for(int j=1; j<21; j++){
                    set.add(Integer.toString(j));
                }
            }
        }
        System.out.print(sb);
    }

}
