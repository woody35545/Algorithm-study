import java.io.*;
import java.util.*;
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        int numA = Integer.parseInt(st.nextToken());
        int numB = Integer.parseInt(st.nextToken());

        Set<Integer> setA = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<numA; i++){
            setA.add(Integer.parseInt(st.nextToken()));
        }

        Set<Integer> setB = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<numB; i++){
            setB.add(Integer.parseInt(st.nextToken()));
        }

        setA.removeAll(setB);

        List<Integer> resultList = new ArrayList<>();

        for(var item:setA){
            resultList.add(item);
        }

        Collections.sort(resultList);

        StringBuilder sb = new StringBuilder();
        sb.append(resultList.size()).append("\n");

        for(int i=0; i<resultList.size(); i++){
            sb.append(resultList.get(i)).append(" ");
        }
        System.out.print(sb);

    }
}
