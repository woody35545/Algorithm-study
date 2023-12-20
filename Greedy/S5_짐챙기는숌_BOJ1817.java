import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {


    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int boxMaxWeight = Integer.parseInt(st.nextToken());

        int[] bookWeights = new int[N];

        if(N > 0)
            st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            bookWeights[i] = Integer.parseInt(st.nextToken());
        }

        int currentWeight = 0;

        // 사용한 박스 개수

        int boxCount = 1;
        for(int i=0; i<N; i++){
            currentWeight += bookWeights[i];
            if(currentWeight > boxMaxWeight){
                boxCount ++;
                currentWeight = bookWeights[i];
            }
        }

        if(N==0) boxCount = 0;

        System.out.print(boxCount);
    }

}
