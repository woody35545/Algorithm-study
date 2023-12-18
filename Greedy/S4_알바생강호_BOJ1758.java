import java.io.*;
import java.util.*;

/** 
* 등수가 뒤로 밀려날수록 팁은 줄어드는데 아무리 줄어들어도 0 밑으로 내려가지 않는다. 
* 따라서 팁을 적게 주려고 한 사람일수록 후순위에 위치하도록 배치를 변경하면 팁을 최대로 받을 수 있다
*/ 
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        // 사람별 팁 주려고하는 금액
        Integer[] tips = new Integer[N];

        // 받은 팁
        long result = 0L;

        for(int i=0; i<N; i++){
            tips[i] = Integer.parseInt(br.readLine());
        }

        // 팁 많이 주는 사람이 먼저 줄서도록 정렬
        Arrays.sort(tips,Collections.reverseOrder());

        // 팁 계산, 팁: 원래 주려고 생각했던 돈 - (받은 등수 - 1)
        for(int i=0; i<N; i++){
            int currentTip = tips[i] - i;
            if(currentTip < 0){
                currentTip = 0;
            }

            result += currentTip;
        }

        System.out.print(result);
    }
}
