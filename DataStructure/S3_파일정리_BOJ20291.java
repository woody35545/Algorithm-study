import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();



    public static void main(String[] args) throws IOException {
        HashMap<String, Integer> map = new HashMap<>();

        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){

            String[] tokens = br.readLine().split("\\.");

            if(!map.containsKey(tokens[1])){
                map.put(tokens[1], 1);
            }else {
                map.put(tokens[1], map.get(tokens[1]) + 1);
            }
        }

        ArrayList<String> fileNames = new ArrayList<>();

        for(var elem : map.keySet()){
            fileNames.add(elem);
        }

        Collections.sort(fileNames);

        for(var elem : fileNames){
            sb.append(elem).append(" ").append(map.get(elem)).append("\n");
        }

        System.out.print(sb);

    }
}
