package 좌표정렬하기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;

class Pos{
    public int x;
    public int y;

    public Pos(int x, int y) {
        this.x = x;
        this.y = y;
    }

}

class posComparator implements Comparator<Pos>{
    @Override
    public int compare(Pos a, Pos b){
        if(a.x != b.x){
            return a.x - b.x;
        }
        else{
            return a.y - b.y;
        }
    }

}

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static ArrayList<Pos> posList = new ArrayList<>();
    public static void main(String[] args) throws IOException{
        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            posList.add(new Pos(x,y));
        }

        posList.sort(new posComparator());

        StringBuilder sb = new StringBuilder();

        for(Pos p : posList){
            sb.append(p.x).append(" ").append(p.y).append("\n");
        }

        System.out.print(sb);
    }
}
