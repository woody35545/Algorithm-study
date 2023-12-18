import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    static int N;
    static int[] numbers;
    static int[] D;

    public static void dp(){
        for(int i=0; i<N; i++){
            for(int j=0; j<i; j++){
                if(numbers[i] > numbers[j]){
                    D[i] = Math.max(D[i], D[j] + 1);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException{
        N = Integer.parseInt(br.readLine());

        numbers = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        D = new int[N];
        Arrays.fill(D,1);

        dp();
        Arrays.sort(D);
        System.out.print(D[D.length-1]);
    }
}
