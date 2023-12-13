import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {

        HashSet<String> keywordMemo = new HashSet<>();

        st = new StringTokenizer(br.readLine());


        // 메모장에 쓴 키워드 개수
        int N = Integer.parseInt(st.nextToken());

        // 블로그에 쓴 키워드 개수
        int M = Integer.parseInt(st.nextToken());

        for(int i=0; i<N; i++){
            keywordMemo.add(br.readLine());
        }

        for(int i=0; i<M; i++){
            String[] keywords = br.readLine().split(",");
            for(int j=0; j<keywords.length; j++){
                if(keywordMemo.contains(keywords[j])){
                    keywordMemo.remove(keywords[j]);
                }
            }

            sb.append(keywordMemo.size()).append("\n");
        }
        System.out.print(sb);
    }
}
