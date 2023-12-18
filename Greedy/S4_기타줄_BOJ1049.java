import java.io.*;
import java.util.*;

    /*
    
    if(가장 싼 낱개 가격 * 6 < 가장 싼 패키지 가격){
        전부다 가장 싼 낱개로 구매	
    }
    else{
        최대한 가장 싼 패키지로 구매하고, 남은 것만 가장 싼 낱개 가격으로 구매
        하지만, 만약 남은 낱개를 낱개로 사는 비용보다 패키지 1개를 사는게 저렴하다면 패키지 한개를 더 사야 최소)
    }
     */

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        int packageMinCost = Integer.MAX_VALUE;
        int singleMinCost =  Integer.MAX_VALUE;

        st = new StringTokenizer(br.readLine());

        // 끊어진 줄 개수
        int N = Integer.parseInt(st.nextToken());

        // 브랜드 수
        int M = Integer.parseInt(st.nextToken());

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int currentPackageCost = Integer.parseInt(st.nextToken());
            int currentSigleCost = Integer.parseInt(st.nextToken());

            if(currentPackageCost < packageMinCost){
                packageMinCost = currentPackageCost;
            }

            if(currentSigleCost < singleMinCost){
                singleMinCost = currentSigleCost;
            }
        }

        int result = 0;
        // 가장 싼 낱개 가격으로 6개 사는 것과 가장 싼 패키지 가격 비교
        if(singleMinCost*6 < packageMinCost){
            // 만약 가장 싼 낱개 가격 6개가 더 싸다면, 전부 낱개로 구매
            result = singleMinCost * N;
        }else{
            // 낱개로 6개 사는 것보다 패키지 하나가 싸다면,
            // 최대한 가장 싼 패키지로 구매하고, 남은 것만 가장 싼 낱개 가격으로 구매

            // 최대한 패키지로 구매
            result += N/6 * packageMinCost;
            int singleCost = N%6 * singleMinCost;
            if(singleCost > packageMinCost){
                // 만약에 남은 낱개를 낱개로 사는 비용이 패키지 비용보다 비싸면 그냥 패키지 한개를 구매하는 것이 더 유리
                result += packageMinCost;
            }else{
                // 남은 낱개 구매 비용이 패키지 하나보다 싸다면, 낱개로 구매
                result += singleCost;
            }
        }

        System.out.print(result);
    }
}
