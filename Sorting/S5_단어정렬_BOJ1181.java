import java.io.*;
import java.util.*;

class CustomComparator implements Comparator<String>{
    @Override
    public int compare(String a, String b){
        /**
         * 길이가 짧은 것부터
         * 길이가 같으면 사전 순으로
         */
        if(a.length() != b.length()){
            return a.length() - b.length();
        }
        else{
            return a.compareTo(b);
        }
    }
}

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static HashSet<String> wordSet = new HashSet<>();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        
        for(int i=0; i<N; i++){
            wordSet.add(br.readLine());
        }

        ArrayList<String> wordList = new ArrayList<String>(wordSet);
        Collections.sort(wordList, new CustomComparator());

        for(var elem : wordList){
            sb.append(elem).append("\n");
        }
        System.out.print(sb);
    }
}
