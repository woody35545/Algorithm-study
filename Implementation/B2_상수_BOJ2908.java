import java.io.*;
import java.util.*;
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        String a = st.nextToken();
        String b = st.nextToken();

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<a.length(); i++){
            sb.append(a.charAt(a.length()-1-i));
        }

        int aReverse = Integer.parseInt(sb.toString());

        sb = new StringBuilder();
        for(int i=0; i<b.length(); i++){
            sb.append(b.charAt(b.length()-1-i));
        }
        int bReverse = Integer.parseInt(sb.toString());
        System.out.print(Math.max(aReverse,bReverse));
    }
}
