import java.io.*;
import java.util.*;

public class Main {

        static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        static StringTokenizer st;
        public static void main(String[] args) throws IOException{
           st = new StringTokenizer(br.readLine());
           int N = Integer.parseInt(st.nextToken());
           int d = Integer.parseInt(st.nextToken());
           int count = 0;
           for(int i=1; i<N+1; i++){
               // current = "120"
               String current = Integer.toString(i);
               for(int j=0; j<current.length(); j++){
                   if(Integer.parseInt(Character.toString(current.charAt(j))) == d){
                     count ++;
                   }
               }
           }
            System.out.print(count);
        }
    }
