import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    /**
     * 현재 위치에서 그대로 이동할 경우 |A-B| 만큼 움직여야 한다.
     * 만약 즐겨찾기 favorite[i] 중에서 |A-B| > |fovorite[i]-B|인 i가 존재하면 일단 즐겨찾기을 눌러 이동한다(버튼 1회 누름).
     * 즐겨찾기로 이동했다면 |fovorite[i]-B|회 만큼 버튼을 추가로 눌러줘야한다.
     * 모든 즐겨찾기를 탐색한 후에도 현재 위치에서 이동하는게 최소일 경우에는 |A-B|번 버튼을 눌러줘야한다.
     */
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        int N = Integer.parseInt(br.readLine());

        // 버튼 누른 횟수
        int count = 0;

        int[] favorites = new int[N];

        for(int i=0; i<N; i++){
            favorites[i] = Integer.parseInt(br.readLine());
        }


        int minDistance = Math.abs(start-end);
        for(int i=0; i<favorites.length; i++){
            int currentDiff = Math.abs(favorites[i] - end);

            if(minDistance > currentDiff){
                minDistance = currentDiff;
            }
        }
        if(minDistance != Math.abs(start-end)){
            count = 1 + minDistance;
        }
        else {
            count = minDistance;
        }
        System.out.print(count);
    }
}
