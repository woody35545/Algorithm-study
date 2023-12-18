import java.io.*;
import java.util.*;

/*
* 처음에 Wrapper Class인 Long으로 구현후, 두 값이 다른지 비교할 때 != 연산자로 비교했다가 틀렸다.
* 이후 primitive 타입인 long으로 바꾸어서 맞았다.
* Wrapper Class는 reference 타입이므로, 값비교시 equals로 비교해주어야 함에 주의해야할 것 같다
*/

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    static long A;
    static long B;

    public static int greedy(){
        /**
         * 1. 숫자 끝이 1이라면 1을 제거하는게 최선
         * 2. 숫자 끝이 1이 아니라면 2로 나누는게 최선
         */

        int count = 0; // 연산 횟수
        while(A < B){

            // 마지막 숫자 확인을 위해 문자열 변환, 152 -> "152"
            String intToStr = Long.toString(B);

            if(intToStr.charAt(intToStr.length()-1) == '1'){
                // 숫자 끝이 1이라면 1을 제거하는게 최선
                B = Long.parseLong(intToStr.substring(0, intToStr.length()-1));
            }

            else{
                // 숫자 끝이 1이 아니라면 2로 나누는게 최선

                // 만약 숫자 끝이 1이 아니고, 2로 나누어 떨어지지도 않는다면 정수인 A를 만들 수 없다.
                if(B%2 != 0){
                    return -1;
                }

                // 2로 나누어 떨어지면 2로 나눈다.
                B /= 2;
            }
            count ++;
        }

        /** A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다.
         * 만들 수 없는 경우에는 -1을 출력한다.
         * */


        if(A!=B){
            // A < B 인데 A!=B 인 경우 B로 A를 만들 수 없음을 의미
            return -1;
        }

        return count + 1;

    }

    public static void main(String[] args) throws IOException{
        st = new StringTokenizer(br.readLine());
        A = Long.parseLong(st.nextToken());
        B = Long.parseLong(st.nextToken());

        System.out.print(greedy());

    }

}
