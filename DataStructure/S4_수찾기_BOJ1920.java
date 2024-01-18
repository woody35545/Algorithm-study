import javax.swing.*;
import java.io.*;
import java.util.*;

/*
이분 탐색으로 풀라고 낸 문제인 것 같으나 Set 자료구조로도 풀린다.
메모리 제한이 지금보다 더 적다면 이분 탐색으로 풀어야 통과할 것 같다.
*/

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    static LinkedHashSet<Integer> numberSet = new LinkedHashSet<>();

    public static void main(String[] args) throws IOException {

        int N = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine()); // 4 1 5 2 3

        for (int i = 0; i < N; i++) {
            numberSet.add(Integer.parseInt(st.nextToken()));
        }

        int M = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i<M; i++) {
            if (numberSet.contains(Integer.parseInt(st.nextToken()))) {
                sb.append(1).append("\n");
            } else {
                sb.append(0).append("\n");
            }
        }

        System.out.print(sb);
    }
}
