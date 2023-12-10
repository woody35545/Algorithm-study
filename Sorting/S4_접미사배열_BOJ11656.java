import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<String> postfixList = new ArrayList<>();
        String S = br.readLine();

        for (int i=0; i<S.length(); i++){
            postfixList.add(S.substring(i, S.length()));
        }

        Collections.sort(postfixList);

        StringBuilder sb = new StringBuilder();

        for(String s : postfixList){
            sb.append(s).append("\n");
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

}
