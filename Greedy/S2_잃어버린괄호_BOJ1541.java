import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        // equation ~> 55-50+40-60+30+10
        String equation = br.readLine();
        // 괄호를 적절히 삽입했을 때 최종 연산 결과를 저장하기 위한 변수
        int totalSum = 0;

        // '-' 기준으로 분리하기 위한 StringTokenizer
        StringTokenizer subtractionSt = new StringTokenizer(equation, "-");

        int count = 0;

        while(subtractionSt.hasMoreTokens()){
            // current ~> "55" -> "50+40" -> "60+30+10"
            String current = subtractionSt.nextToken();

            StringTokenizer additionSt = new StringTokenizer(current, "+");

            // temp: current의 연산 결과, ex) 50+40 = 90
            int temp = 0;
            while(additionSt.hasMoreTokens()){
                temp += Integer.parseInt(additionSt.nextToken());
            }
            // 첫번째 숫자인 경우, 첫번째 숫자로 초기화
            if(count == 0){
                totalSum = temp;
            }else{
                // 이후는 전체 결과에서 빼주므로써 -부터 다음 -전까지의 숫자를 괄호로 묶은 효과를 줌
                totalSum -= temp;
            }
            count ++;

        }

        System.out.print(totalSum);
    }
}
