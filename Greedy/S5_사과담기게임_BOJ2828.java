import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        // 움직인 거리
        int result = 0;

        int N = Integer.parseInt(st.nextToken());

        // 바구니 크기
        int M = Integer.parseInt(st.nextToken());

        // 바구니 초기 시작점과 끝점
        int basketStart = 0;
        int basketEnd = M-1;

        // 떨어지는 사과 개수
        int J = Integer.parseInt(br.readLine());

        for(int i=0; i<J; i++){
            int applePosition = Integer.parseInt(br.readLine()) - 1;


            // 1. 바구나 안에 떨어지는 경우
            if(basketStart <= applePosition && applePosition <= basketEnd){
                // 움직일 필요 없음
                continue;
            }else{
                // 2. 바구니 밖에 떨어지는 경우
                if(applePosition < basketStart) {
                    // 2-1. 바구니 왼쪽에 떨어지는 경우

                    // 바구니 시작점이 사과가 떨어진 위치에 도달하도록 하는 경우가 이동거리 최소
                    int diff = basketStart - applePosition;

                    // 해당 거리만큼 왼쪽으로 이동 후, 좌표로 갱신
                    basketStart -= diff;
                    basketEnd -= diff;

                    // 현재까지 움직인 거리 갱신
                    result += diff;
                }
                else if(applePosition > basketEnd){
                    // 2-2. 바구니 오른쪽에 떨어지는 경우

                    // 바구니 끝점이 사과가 떨어진 위치에 도달하도록 하는 경우가 이동거리 최소
                    int diff = applePosition - basketEnd;

                    // 해당 거리만큼 오른쪽으로 이동 후, 좌표 갱신
                    basketStart += diff;
                    basketEnd += diff;

                    result += diff;
                }
            }
        }

        System.out.print(result);
    }
}
