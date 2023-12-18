import java.io.*;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

        static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        static StringTokenizer st;
        static StringBuilder sb = new StringBuilder();
        public static void main(String[] args) throws IOException{
            int N = Integer.parseInt(br.readLine());
            PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
                @Override
                public int compare(Integer a, Integer b) {
                    int abs_a = Math.abs(a);
                    int abs_b = Math.abs(b);

                    if (abs_a == abs_b) {
                        if (a > b) {
                            return 1;
                        } else if (a < b) {
                            return -1;
                        }
                    }
                    return abs_a - abs_b;
                }
            });

            for(int i=0; i<N; i++){
                int num = Integer.parseInt(br.readLine());

                if(num == 0){
                    if(pq.size() == 0){
                        sb.append(0).append("\n");
                    }else{
                        sb.append(pq.remove()).append("\n");
                    }
                }
                else{
                    pq.add(num);
                }
            }
            System.out.print(sb);
        }
    }
