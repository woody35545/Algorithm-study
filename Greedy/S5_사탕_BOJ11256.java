import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    /**
     * 담을 수 있는 용량이 가장 큰 상자부터 선택해서 담아주면 상자 개수가 최소가 된다.
     */
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


    static int minBoxCount(int[] boxSize, int numOfCandy){
        Integer[] boxSizeInteger = new Integer[boxSize.length];
        for(int i=0; i<boxSize.length; i++){
            boxSizeInteger[i] = Integer.valueOf(boxSize[i]);
        }

        Arrays.sort(boxSizeInteger, Collections.reverseOrder());
        
        // 사용한 박스 개수
        int count = 0;

        for(int i=0; i<boxSizeInteger.length; i++){
            if(numOfCandy <= 0) break;
            numOfCandy -= boxSizeInteger[i];
            count++;
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int numOfCandy = Integer.parseInt(st.nextToken());
            int numOfBox = Integer.parseInt(st.nextToken());

            // 상자별 담을 수 있는 사탕 개수
            int[] boxSize = new int[numOfBox];

            for(int i=0; i<numOfBox; i++){
                st = new StringTokenizer(br.readLine());
                boxSize[i] = Integer.parseInt(st.nextToken()) * Integer.parseInt(st.nextToken());
            }

            sb.append(minBoxCount(boxSize, numOfCandy)).append("\n");
        }
        System.out.print(sb);
    }

}
