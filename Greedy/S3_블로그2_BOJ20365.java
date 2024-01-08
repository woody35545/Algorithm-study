import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    /**
     * 최소 횟수: 구역 수가 더 적은 색의 구역 개수 + 1
     *
     * 전체를 구역수가 더 많은 색깔로 칠한 후(1회), 구역수가 더 적은 색깔의 구역 수만큼 칠해 준다.
     *
     * 예시)
     * RRBBBRRBRR
     *
     * → R의 구역수: 3개
     * → B의 구역수: 2개
     *
     * 1. R로 전부 뒤집음(1회) → RRRRRRRRRRR
     * 2. B로 칠해야하는 구역수만큼 칠함(2회) → RRBBBRRBRR
     *
     * 따라서 최소횟수 : 3회
     */
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException{
        int N = Integer.parseInt(br.readLine());
        String inputStr = br.readLine();

        int bCount = 0;
        int rCount = 0;
        for(int i=0; i<N; i++){
            if(inputStr.charAt(i) == 'B'){
                bCount++;
            }
            else{
                rCount++;
            }
        }

        int result = 0;

        String[] splittedByR = inputStr.split("R");
        int splittedByRLength = 0;
        for(int i=0; i<splittedByR.length; i++){
            if(!splittedByR[i].equals("")){
                splittedByRLength++; //
            }
        }


        String[] splittedByB = inputStr.split("B");
        int splittedByBLength = 0;
        for(int i=0; i<splittedByB.length; i++){
            if(!splittedByB[i].equals("")){
                splittedByBLength++; //
            }
        }

        result = Math.min(splittedByBLength,splittedByRLength) + 1;

        System.out.print(result);

    }
}
