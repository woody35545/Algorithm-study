import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        ArrayList<Integer> result = new ArrayList<>();
        for(int i=0; i<5; i++){
            String input = br.readLine();
            if(input.contains("FBI")){
                result.add(i+1);
            }
        }
        if(result.size() == 0){
            System.out.print("HE GOT AWAY!");
        }
        else{
            for(var e : result){
                sb.append(e).append(" ");
            }
            System.out.print(sb);
        }
    }

}
