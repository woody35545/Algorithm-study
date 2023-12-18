import java.io.*;
import java.util.*;

class Country {
    int countryNumber;
    int goldCount;
    int silverCount;
    int bronzeCount;

    int rate;

    public Country(int countryNumber, int goldCount, int silverCount, int bronzeCount) {
        this.countryNumber = countryNumber;
        this.goldCount = goldCount;
        this.silverCount = silverCount;
        this.bronzeCount = bronzeCount;
        this.rate = 0;
    }
}

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        ArrayList<Country> countryList = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            countryList.add(
                    new Country(Integer.parseInt(st.nextToken()),
                            Integer.parseInt(st.nextToken()),
                            Integer.parseInt(st.nextToken()),
                            Integer.parseInt(st.nextToken())));
        }

        Collections.sort(countryList, new Comparator<Country>() {
            @Override
            public int compare(Country a, Country b) {
                if (a.goldCount != b.goldCount) {
                    return -(a.goldCount - b.goldCount);
                } else if (a.silverCount != b.silverCount) {
                    return -(a.silverCount - b.silverCount);
                } else if (a.bronzeCount != b.bronzeCount) {
                    return -(a.bronzeCount - b.bronzeCount);
                } else {
                    return 0;
                }
            }
        });


        int count = 2;
        countryList.get(0).rate = 1;

        for(int i=1; i<countryList.size(); i++){
            Country prev = countryList.get(i-1);
            Country current = countryList.get(i);

            if(prev.goldCount == current.goldCount
                    && prev.silverCount == current.silverCount
                    && prev.bronzeCount == current.bronzeCount){
                current.rate = prev.rate;
                count++;
            }
            else{
                current.rate = count++;
            }
        }
        for(int i=0; i<countryList.size(); i++){
            if(countryList.get(i).countryNumber == K){
                System.out.print(countryList.get(i).rate);
            }
        }
    }

}
