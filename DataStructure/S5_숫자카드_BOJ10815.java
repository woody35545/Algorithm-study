import java.io.*;
import java.util.Arrays;
import java.util.HashMap;

public class Main {

    public static void main(String[] args) throws IOException {
        HashMap<String, String> hashMap = new HashMap<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
       
        int N = Integer.parseInt(br.readLine());
        String[] cards = br.readLine().split(" ");

        for (int i=0; i<cards.length; i++){
            hashMap.put(cards[i], cards[i]);
        }

        int M = Integer.parseInt(br.readLine());

        String[] question = br.readLine().split(" ");

        int[] result = new int[M];

        for (int i=0; i<question.length; i++){

            if(hashMap.containsKey(question[i])){
                result[i] = 1;
            }
            else{
                result[i] = 0;
            }
        }

        for(int i=0; i<result.length; i++){
            System.out.print(result[i] + " ");
        }
    }
}
