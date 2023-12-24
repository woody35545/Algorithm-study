import java.io.*;
import java.util.*;

public class Main {

        static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        static StringTokenizer st;

        static boolean isOk(String str){
            // str ~> "ABCABCBBAAACC"

            HashMap<Character,Integer> map = new HashMap<>();

            for(int i=0; i<str.length(); i++){
                Character currentChar = Character.valueOf(str.charAt(i));
                if(!map.containsKey(currentChar)){
                    map.put(currentChar, 1);
                }else{
                    map.put(currentChar, map.get(currentChar)+1);
                }

                if(map.get(currentChar) == 3){
                    if(i == str.length()-1){
                        return false;
                    }else if(str.charAt(i+1) != currentChar){
                        return false;
                    }
                    // 그다음 문자는 암호문자이므로 카운트 안하고 넘어가기 위해 -1로 초기화
                    map.put(currentChar, -1);
                }
            }
            return true;
        }
        public static void main(String[] args) throws IOException{
           int N = Integer.parseInt(br.readLine());
           StringBuilder sb = new StringBuilder();
           for(int i=0; i<N; i++){
               String str = br.readLine();
               if(isOk(str)){
                   sb.append("OK").append("\n");
               }
                else{
                    sb.append("FAKE").append("\n");
                }
           }
            System.out.print(sb);
        }
    }
