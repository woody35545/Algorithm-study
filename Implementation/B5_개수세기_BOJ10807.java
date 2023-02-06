/* 23.02.06 - 입력되는 숫자의 범위를 제대로 읽지 않아서 IndexOutOfBound가 발생하였다. 문제가 쉬워도 조건을 꼼꼼히 읽을 필요가 있을 것 같다. */ 

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[201]; // index 0~100 , 0은 무시

        for (int i = 0; i < N; i++) {
            arr[sc.nextInt() + 100]++;
        }
        System.out.print(arr[sc.nextInt() + 100]);
         }
}

