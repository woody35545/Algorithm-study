import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    public static void main(String[] args) throws IOException {
        Deque<String> deque = new ArrayDeque<>();

        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            String[] tokens = br.readLine().split(" ");

            if(tokens[0].equals("1")){
                deque.addFirst(tokens[1]);
            }
            else if(tokens[0].equals("2")){
                deque.addLast(tokens[1]);
            }
            else if (tokens[0].equals("3")) {
                if (deque.isEmpty()) {
                    sb.append("-1").append("\n");

                } else {
                    sb.append(deque.removeFirst()).append("\n");
                }

            }
            else if(tokens[0].equals("4")){
                if(deque.isEmpty()){
                    sb.append("-1").append("\n");
                }
                else{
                    sb.append(deque.removeLast()).append("\n");
                }
            }
            else if(tokens[0].equals("5")) {
                sb.append(deque.size()).append("\n");
            }

            else if(tokens[0].equals("6")) {
                if(deque.isEmpty()){
                    sb.append("1").append("\n");
                } else {
                    sb.append("0").append("\n");
                }
            }

            else if(tokens[0].equals("7")) {
                if(deque.isEmpty()){
                    sb.append("-1").append("\n");
                } else {
                    sb.append(deque.getFirst()).append("\n");
                }
            }

            else if(tokens[0].equals("8")) {
                if(deque.isEmpty()){
                    sb.append("-1").append("\n");

                } else {
                    sb.append(deque.getLast()).append("\n");
                }
            }

        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

}
