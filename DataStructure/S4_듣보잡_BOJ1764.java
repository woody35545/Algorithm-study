import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashSet<String> set1 = new HashSet<>();
        HashSet<String> set2 = new HashSet<>();

        for(int i=0; i<N; i++){
            set1.add(br.readLine());
        }

        for(int i=0; i<M; i++){
            set2.add(br.readLine());
        }

        // 교집합 구하기
        HashSet<String> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);

        // 정렬
        ArrayList<String> intersactionToList = new ArrayList<>(intersection);
        Collections.sort(intersactionToList);

        StringBuilder sb = new StringBuilder();

        sb.append(intersactionToList.size()).append("\n");

        for(String s : intersactionToList){
            sb.append(s).append("\n");
        }

        System.out.print(sb);
    }
}
