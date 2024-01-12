import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class Main {

    /**
     * 가장 비싼순서대로 최대한 3개씩 묶으면 최소가격이 된다.
     */
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        Integer[] costs = new Integer[N];
        // 지불해야하는 전체 가격
        int totalCost = 0;
        for(int i=0; i<costs.length; i++){
            costs[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(costs, Collections.reverseOrder());

        int count = 0;
        // 3번째 가격은 버린다.
        for(int i=0; i<costs.length; i++){
            if((i+1)%3 == 0) continue;
            totalCost += costs[i];
        }
        System.out.print(totalCost);
    }

}
