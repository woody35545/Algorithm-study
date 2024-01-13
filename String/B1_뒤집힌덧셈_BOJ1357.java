import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int reverseNumber(int num){
        String numStr = String.valueOf(num);
        // 숫자 뒤집기
        StringBuilder reverseSb = new StringBuilder();
        for(int i=numStr.length()-1; i>=0; i--){
            reverseSb.append(numStr.charAt(i));
        }
        return Integer.parseInt(reverseSb.toString());
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer num1 = Integer.parseInt(st.nextToken());
        Integer num2 = Integer.parseInt(st.nextToken());

        System.out.println(reverseNumber(reverseNumber(num1) + reverseNumber(num2)));

    }
}
