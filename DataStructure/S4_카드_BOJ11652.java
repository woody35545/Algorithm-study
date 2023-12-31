import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        long N = Long.parseLong(br.readLine());
        // number : count
        HashMap<Long, Long> map = new HashMap<>();

        Long currentMaxCount = 0L;
        Long currentMaxValue = 0L;

        for(int i=0; i<N; i++){
            Long num = Long.parseLong(br.readLine());
            map.put(num, map.getOrDefault(num, Long.valueOf(0)) + 1);

            if(map.get(num) > currentMaxCount){
                currentMaxCount = map.get(num);
                currentMaxValue = num;
            }
            else if(map.get(num).equals(currentMaxCount)){
                currentMaxValue = Math.min(currentMaxValue, num);
            }
        }
        System.out.print(currentMaxValue);
    }
}
