import java.io.*;
import java.util.LinkedHashMap;
import java.util.StringTokenizer;

public class Main {
    public static boolean isNumber(String a) {
        try {
            Integer.parseInt(a);
            return true;
        }catch(Exception e){
            return false;
        }
    }
        static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        static StringTokenizer st;
        static StringBuilder sb = new StringBuilder();
        public static void main(String[] args) throws IOException{
            LinkedHashMap<String, Integer> map = new LinkedHashMap();
            LinkedHashMap<Integer, String> reverseMap = new LinkedHashMap();

            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            for(int i=0; i<N; i++){
                String name = br.readLine();
                map.put(name, i+1);
                reverseMap.put(i+1, name);
            }

            for(int i=0; i<M; i++){
                String question = br.readLine();
                if(isNumber(question)){
                    sb.append(reverseMap.get(Integer.parseInt(question))).append("\n");
                }
                else{
                    sb.append(map.get(question)).append("\n");
                }
            }
            System.out.print(sb);
        }
    }
