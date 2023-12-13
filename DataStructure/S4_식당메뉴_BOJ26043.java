import java.io.*;
import java.util.*;

class Person{
    int personNumber;
    int favoriteFood;

    public Person(int personNumber, int favoriteFood) {
        this.personNumber = personNumber;
        this.favoriteFood = favoriteFood;
    }
}

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    static ArrayList<Integer> AList = new ArrayList<>();
    static ArrayList<Integer> BList = new ArrayList<>();
    static ArrayList<Integer> CList = new ArrayList<>();

    static final int PERSON_INFO = 1;
    static final int FOOD_INFO = 2;
    static Queue<Person> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            // 들어온 정보 유형
            int type = Integer.parseInt(st.nextToken());

            if(type == PERSON_INFO){
                // 줄서려는 사람에 대한 정보인 경우

                // 사람 번호
                int personNumber = Integer.parseInt(st.nextToken());
                // 좋아하는 음식 정보
                int favoriteFoodNumber = Integer.parseInt(st.nextToken());

                queue.add(new Person(personNumber, favoriteFoodNumber));
            }

            else if(type == FOOD_INFO){
                // 나온 음식에 대한 정보인 경우
                int foodNumber = Integer.parseInt(st.nextToken());

                // 현재 줄에서 가장 앞에있는(오른쪽) 사람에게 음식 제공
                Person p = queue.remove();

                if(p.favoriteFood == foodNumber){
                    // 제공된 음식이 좋아하는 음식과 일치한다면 A 리스트에 추가
                    AList.add(p.personNumber);
                }
                else{
                    // 좋아하는 음식이 아니라면 B 리스트에 추가
                    BList.add(p.personNumber);
                }
            }
        }

        while(!queue.isEmpty()){
            // 끝날때까지 음식을 받지 못한 사람은 C 리스트에 추가
            CList.add(queue.remove().personNumber);
        }

        // 각 리스트를 오름차순 정렬
        Collections.sort(AList);
        Collections.sort(BList);
        Collections.sort(CList);

        // A 리스트 출력
        if(AList.isEmpty()){
            sb.append("None");
        }else {
            for (var elem : AList) {
                sb.append(elem).append(" ");
            }
        }
        sb.append("\n");

        // B 리스트 출력
        if(BList.isEmpty()){
            sb.append("None");
        }else {
            for (var elem : BList) {
                sb.append(elem).append(" ");
            }
        }
        sb.append("\n");

        // C 리스트 출력
        if(CList.isEmpty()){
            sb.append("None");
        }else {
            for (var elem : CList) {
                sb.append(elem).append(" ");
            }
        }

        System.out.print(sb);
    }


}
