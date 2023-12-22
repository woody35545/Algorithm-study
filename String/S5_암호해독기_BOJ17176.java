import java.io.*;
import java.util.*;
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());

        HashMap<Character, Integer> preparedMap = new HashMap<>();
        HashMap<Character, Integer> resultMap = new HashMap<>();

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            int currentInt = Integer.parseInt(st.nextToken());
            char curChar = '\u0000';

            if(currentInt<27){ // 대문자
                curChar = (char)(currentInt+64);
            }else if(27 <= currentInt && currentInt<= 52){
                // 소문자
                curChar = (char)(currentInt+70);
            }else if(currentInt == 0){
                // 띄어쓰기
                curChar= ' ';
            }

//            System.out.println(String.format("curInt: %d, curChar: %c", currentInt,curChar));

            if(!preparedMap.containsKey(curChar)) {
                preparedMap.put(curChar, 1);
            }else {
                preparedMap.put(curChar, preparedMap.get(curChar)+1);
            }
        }

        String resultString = br.readLine();
        for(int i=0; i<resultString.length(); i++){
            char curChar = resultString.charAt(i);
            if(curChar == ' '){
                curChar = '@';
            }
            if(!resultMap.containsKey(curChar)){
                resultMap.put(curChar,1);
            }else {
                resultMap.put(curChar,resultMap.get(curChar)+1);
            }
        }
//        for(char c : preparedMap.keySet()){
//            System.out.println(String.format("%c:%d, ",c,preparedMap.get(c)));
//        }
        // preparedMap의 각 개수가 resultMap 보다 더 많아야함
        boolean result = true;
        for(char c : resultMap.keySet()){
            if(!preparedMap.containsKey(c)){
                result = false;
            }
            else if(resultMap.get(c) > preparedMap.get(c)){
                result = false;
            }
        }
        if(result){
            System.out.print("y");
        }else {
            System.out.print("n");
        }
    }
}
