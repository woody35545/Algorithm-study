import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();


        for(int i=0; i<N; i++){
            for(int j=N-i-1; j>0; j--){
                sb.append(" ");
            }

            sb.append("*");

            for(int j=0; j<i; j++){
                sb.append("**");
            }
            sb.append("\n");
        }

        for(int i=0; i<N-1; i++){
            for(int j=0; j<i+1; j++){
                sb.append(" ");
            }

            sb.append("*");

            for(int j=0; j<N-i-2; j++){
                sb.append("**");
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }
}
