import java.io.*;
import java.util.*;

public class Main {

        static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        static StringTokenizer st;

        public static void main(String[] args) throws IOException {
            String inputStr = br.readLine();

            String upperStr = inputStr.toUpperCase();
            HashMap<Character, Integer> map = new HashMap<>();

            for(int i=0; i<upperStr.length(); i++){
                Character curChar = upperStr.charAt(i);

                if(!map.containsKey(curChar)){
                    map.put(curChar, 1);
                }
                else{
                    map.put(curChar, map.get(curChar) + 1);
                }
            }
            int tmpMax = 0;
            Character tmpMaxChar = '\u0000';
            for(var e : map.keySet()){
                if(tmpMax < map.get(e)){
                    tmpMax = map.get(e);
                    tmpMaxChar = e;
                }
            }
            int cnt = 0;
            for(var e : map.keySet()){
                if(map.get(e) == tmpMax){
                    cnt ++;
                }
            }

            if(cnt > 1){
                System.out.print("?");
            }else{
                System.out.print(tmpMaxChar);
            }
        }

    }
