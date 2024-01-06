import java.io.*;
import java.util.*;
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        String[] inputStrs = br.readLine().trim().split(" ");
        if (inputStrs.length==1 && inputStrs[0].equals("")) {
            System.out.print(0);
        } else {
            System.out.print(inputStrs.length);
        }
    }
}
