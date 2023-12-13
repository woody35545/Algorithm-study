import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        HashSet<Integer> setA = new HashSet<>();
        HashSet<Integer> setB = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        int numA = Integer.parseInt(st.nextToken());
        int numB = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<numA; i++){
            setA.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<numB; i++){
            setB.add(Integer.parseInt(st.nextToken()));
        }

        // setA - setB 개수
        int cntA = 0;
        for(var elem : setA){
            if(!setB.contains(elem)){
                cntA ++;
            }
        }

        // setB - setA 개수
        int cntB = 0;
        for(var elem : setB){
            if(!setA.contains(elem)){
                cntB ++;
            }
        }
        System.out.print(cntA+cntB);
    }
}
